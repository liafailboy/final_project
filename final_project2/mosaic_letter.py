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

SRC_FOLDER = "source/images"
OUT_FOLDER = "output"

ORG_IMG = cv2.imread("source/image.png")
IMG_FILES = os.listdir(SRC_FOLDER)

IMG_EXTS = set(["png", "jpeg", "jpg", "gif", "tiff", "tif", "raw", "bmp"])

## Every computation happening here.

cv2.imwrite("letter.png",ORG_IMG)