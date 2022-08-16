#include <iostream>
#include <opencv2/opencv.hpp>
int main()
{
    cv::Mat img = cv::imread("./res/front.bmp");
    cv::imshow("img", img);
    cv::waitKey(0);
    std::cout << "hello, world" << std::endl;
    return 0;
}