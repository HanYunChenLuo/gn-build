// Copyright 2014 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include <iostream>

#include "hello_shared.h"
#include "hello_static.h"
#include <opencv2/opencv.hpp>

int main(int argc, char* argv[]) {
    //   printf("%s, %s\n", GetStaticText(), GetSharedText());
    // std::cout << GetStaticText() << ", " << GetSharedText() << std::endl;
    std::cout << GetStaticText() << std::endl;
    std::cout << GetSharedText() << std::endl;
    cv::Mat img = cv::imread("./res/front.bmp");
    cv::imshow("img", img);
    cv::waitKey(0);
    return 0;
}
