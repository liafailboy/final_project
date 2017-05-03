//
//  ViewController.m
//  final_project
//
//  Created by Shotaro Watanabe on 4/24/17.
//  Copyright © 2017 Shotaro Watanabe. All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
    isActive = false;
    camera = [[CvVideoCamera alloc] initWithParentView: imageView];
    camera.defaultAVCaptureDevicePosition = AVCaptureDevicePositionBack;
    camera.defaultAVCaptureSessionPreset = AVCaptureSessionPreset640x480;
    camera.defaultAVCaptureVideoOrientation = AVCaptureVideoOrientationPortrait;
    camera.defaultFPS = 30;
    camera.grayscaleMode = NO;
    camera.delegate = self;
}

- (void)processImage:(cv::Mat &)image {
//    const char* str = [@"HELLO, WORLD! Testing OpenCV on my iPhone" cStringUsingEncoding: NSUTF8StringEncoding];
//    cv::putText(image, str, cv::Point(50, 50), CV_FONT_HERSHEY_PLAIN, 2.0, cv::Scalar(0, 0, 255));
//    
    // Copy original image to the image_copy
    cv::Mat image_copy;
    cvtColor(image, image_copy, CV_BGRA2BGR);
    
    // Copying back to the original image with greyscale process
    cvtColor(image_copy, image, CV_RGB2GRAY);
    
    
}

- (IBAction)startOrStop:(id)sender {
    if (isActive) {
        [camera stop];
        isActive = false;
    } else {
        [camera start];
        isActive = true;
    }
    
}

- (void)viewDidAppear:(BOOL)animated {
    [camera start];
    isActive = true;
}


- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}


@end
