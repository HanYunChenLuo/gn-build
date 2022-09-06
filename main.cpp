// Copyright 2014 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include <iostream>
#include <jni.h>

#include <hello_static.h>
#include <hello_shared.h>

extern "C" JNIEXPORT jstring JNICALL
Java_com_example_test_MainActivity_stringFromJNI(
        JNIEnv* env,
        jobject /* this */) {
    std::string hello = "Hello from C++";
    return env->NewStringUTF(hello.c_str());
}

int main(int argc, char* argv[]) {
    std::cout << GetStaticText() << std::endl;
    std::cout << GetSharedText() << std::endl;
    return 0;
}
