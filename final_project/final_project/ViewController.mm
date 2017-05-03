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
    camera = [[CvVideoCamera alloc] initWithParentView: imageView];
    camera.defaultAVCaptureDevicePosition = AVCaptureDevicePositionBack;
    camera.defaultAVCaptureSessionPreset = AVCaptureSessionPreset640x480;
    camera.defaultAVCaptureVideoOrientation = AVCaptureVideoOrientationPortrait;
    camera.defaultFPS = 30;
    camera.grayscaleMode = NO;
    camera.delegate = self;
}

- (void)processImage:(cv::Mat &)image {
    const char* str = [@"HELLO, WORLD! Testing OpenCV on my iPhone" cStringUsingEncoding: NSUTF8StringEncoding];
    cv::putText(image, str, cv::Point(100, 100), CV_FONT_HERSHEY_PLAIN, 2.0, cv::Scalar(0, 0, 255));
}

- (void)viewDidAppear:(BOOL)animated {
    [camera start];
}


- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}


@end
