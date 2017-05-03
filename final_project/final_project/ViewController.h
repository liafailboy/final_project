//
//  ViewController.h
//  final_project
//
//  Created by Shotaro Watanabe on 4/24/17.
//  Copyright © 2017 Shotaro Watanabe. All rights reserved.
//

#import <UIKit/UIKit.h>
#import <opencv2/highgui/cap_ios.h>

@interface ViewController : UIViewController <CvVideoCameraDelegate>{
    IBOutlet UIImageView *imageView;
    CvVideoCamera *camera;
}


@end

