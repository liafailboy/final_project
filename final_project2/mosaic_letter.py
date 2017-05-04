# Final Project
# Shotaro Watanabe

# My project proposal was to make AR recognition work on iOS,
# but I could not figure out well to create the app,
# so I decidec to go back to Python and create mosaic letter from your input photos.
# Users will be able to select the input photos and create mosaic letters from it.

import cv2

import os

import numpy as np
import scipy as sp

import math

## File management
SRC_FOLDER = "source/images"

ORG_IMG = cv2.imread("source/input4.jpg")
IMG_FILES = os.listdir(SRC_FOLDER)

NUMBER_OF_IMAGE = 50

## IMAGE SIZE to be made
ORIGINAL_WIDTH = 600
ORIGINAL_HEIGHT = 450

## ORIGINAL INPUT IMAGE SIZE
WIDTH = 8
HEIGHT = 6

counter = 0;

IMG_EXTS = ["png", "jpeg", "jpg", "gif", "tiff", "tif", "raw", "bmp"]

## Every computation happening here.

## Get the average RGB value for the given index range
def getAverageOfBlock(original, index):
	colorSum = np.array([0, 0, 0])
	if index[0] < ORIGINAL_HEIGHT - HEIGHT + 1 and index[1] < ORIGINAL_WIDTH - WIDTH + 1:
		for i in range(index[0], index[0] + HEIGHT):
			for j in range(index[1], index[1] + WIDTH):
				colorSum = np.add(colorSum, original[i, j])

	return colorSum / WIDTH / HEIGHT

## Get the average value of the resized input images
def getAverageOfImages(listOfImages):

	colorSum = np.array([0, 0, 0])
	listOfAverage = []

	for image in listOfImages:
		for i in range(0, image.shape[0]):
			for j in range(0, image.shape[1]):
				colorSum = colorSum + image[i, j]

		numberOfPixels = image.shape[0] * image.shape[1]
		listOfAverage.append(colorSum / numberOfPixels)
		colorSum = np.array([0, 0, 0])
	
	return listOfAverage

## Put the best match image to the certain index of the image
def foundBestImageForIndex(empty, bestImage, index):
	global counter
	counter = counter + 1
	if index[0] < ORIGINAL_HEIGHT - HEIGHT + 1 and index[1] < ORIGINAL_WIDTH - WIDTH + 1:
		for i in range(index[0], index[0] + HEIGHT):
			for j in range(index[1], index[1] + WIDTH):
				empty[i][j] = bestImage[i % HEIGHT, j % WIDTH]

	print "Adding:" + str(counter) + "th photo."

	return empty

## resize the image to speed up processing speed
def createSmallImages(imageFiles):
	listOfImages = []
	listOfResizedImages = []

	for aFile in imageFiles:
		if aFile.split(".")[-1].lower() in IMG_EXTS:
			listOfImages.append(aFile)

	for aImage in listOfImages:
		print "Resizing:" + aImage
		loadedImage = cv2.imread(os.path.join(SRC_FOLDER, aImage))
		listOfResizedImages.append(cv2.resize(loadedImage, (WIDTH, HEIGHT)))

	return listOfResizedImages

## main function to start creating the mosaic picture letter
def createLetter(original, listOfImages):

	imageOfBestMatch = listOfImages[0]
	valueDiff = 0

	letter_image = np.zeros((original.shape[0], original.shape[1], 3))

	for i in range(0, original.shape[0], HEIGHT):
		for j in range(0, original.shape[1], WIDTH):

			smallest = (255**2) * 3
			averageOfBlock = getAverageOfBlock(original, (i, j))
			averageOfImages = getAverageOfImages(listOfImages)

			for k in range(0, len(averageOfImages)):
				rDiff = (averageOfImages[k][0] - averageOfBlock[0])**2
				gDiff = (averageOfImages[k][1] - averageOfBlock[1])**2
				bDiff = (averageOfImages[k][2] - averageOfBlock[2])**2
				valueDiff = np.sqrt(rDiff+gDiff+bDiff)

				if valueDiff < smallest:
					smallest = valueDiff
					imageOfBestMatch = listOfImages[k]

			letter_image = foundBestImageForIndex(letter_image, imageOfBestMatch, (i, j))

	return letter_image

final_letter = createLetter(ORG_IMG, createSmallImages(IMG_FILES))

cv2.imwrite("letter.png", final_letter)