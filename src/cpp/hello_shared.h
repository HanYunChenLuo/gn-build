// Copyright 2014 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef TOOLS_GN_EXAMPLE_HELLO_SHARED_H_
#define TOOLS_GN_EXAMPLE_HELLO_SHARED_H_

#define DLL_EXPORT __attribute__((visibility("default")))
#define DLL_EXPORT_PRIVATE __attribute__((visibility("default")))

DLL_EXPORT const char* GetSharedText();

#endif  // TOOLS_GN_EXAMPLE_HELLO_SHARED_H_
