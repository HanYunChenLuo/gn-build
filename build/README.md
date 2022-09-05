# //build directory for GN-based projects

This project provides a work-in-progress standalone version of the toolchains and configs used by the Chromium project.

## Supported platforms

The toolchains have been tested on the following platforms:

* Linux (GCC/Clang)
* OS X

[![Build Status](https://travis-ci.org/timniederhausen/gn-build.svg?branch=master)](https://travis-ci.org/timniederhausen/gn-build)
[![Build status](https://ci.appveyor.com/api/projects/status/jpot0c7wp6e78lkk/branch/master?svg=true)](https://ci.appveyor.com/project/timniederhausen/gn-build)

The [testsrc](https://github.com/timniederhausen/gn-build/tree/testsrc)
branch contains the test/example project used by the CI tests.

## Reference

### Basic variables

All variables described here are build args and can be overridden in the user's
`args.gn` file.

#### [`//build/config/BUILDCONFIG.gn`](config/BUILDCONFIG.gn)

(these variables are available everywhere)

* `is_debug` (default: true): Toggle between debug and release builds.
* `is_clang` (default: false): Favor Clang over the platform default (GCC/MSVC).
* `is_official_build` (default: !is_debug): Set to enable the official build
  level of optimization. This enables an additional level of optimization above
  release (!is_debug).

#### [`//build/toolchain/clang.gni`](toolchain/clang.gni)

* `use_lld` (default: false): Use the new LLD linker.
  This requires `is_clang` to be true.
* `clang_base_path` (default: ""): The path of your Clang installation folder
  (without /bin). If you use Clang on Windows, you are required to set this,
  as the Clang installation isn't automatically detected.

#### [`//build/toolchain/compiler_version.gni`](toolchain/compiler_version.gni)

* `gcc_version` (default: auto-detected): Version of the GCC compiler.
  **Note:** Auto-detection is toolchain-specific and happens only if GCC is the
  active compiler. <br>
  Format: `major` * 10000 + `minor` * 100 + `patchlevel`
* `clang_version` (default: auto-detected): Version of the Clang compiler.
  **Note:** Auto-detection is toolchain-specific and happens only if Clang is
  the active compiler. <br>
  Format: `major` * 10000 + `minor` * 100 + `patchlevel`

### POSIX toolchain

This is the default toolchain for POSIX operating systems,
which is used for all POSIX systems that don't have special toolchains.

#### [`//build/toolchain/posix/settings.gni`](toolchain/posix/settings.gni)

* `gcc_cc` (default: gcc): Path of the GCC C compiler executable.
  Does not have to be absolute.
* `gcc_cxx` (default: g++): Path of the GCC C++ compiler executable.
  Does not have to be absolute.
* `clang_cc` (default: clang): Path of the Clang C compiler executable.
  Does not have to be absolute. **Note:** If `clang_base_path` is set,
  the default will be `clang_base_path/bin/clang`.
* `clang_cxx` (default: clang++): Path of the Clang C++ compiler executable.
  Does not have to be absolute. **Note:** If `clang_base_path` is set,
  the default will be `clang_base_path/bin/clang++`.

### Mac toolchain

#### [`//build/config/mac/mac_sdk.gni`](config/mac/mac_sdk.gni)

* `mac_sdk_min` (default: "10.10"): Minimum supported version of the Mac SDK.
* `mac_deployment_target` (default: "10.9"): Minimum supported version of OSX.
* `mac_sdk_path` (default: ""): Path to a specific version of the Mac SDK, not
  including a slash at the end. If empty, the path to the lowest version
  greater than or equal to `mac_sdk_min` is used.
* `mac_sdk_name` (default: "macosx"): The SDK name as accepted by xcodebuild.

## Recommended workflow

Fork this repo and add it as a submodule/subtree/`DEPS`-entry to your project.
This way you can modify every part of the `//build` directory while still being
able to easily merge upstream changes (e.g. support for new GN features that
you don't want to implement yourself.)

To ease sharing/composition of projects using this `//build` repo,
it is recommended that you refrain from modifying large parts of the toolchains/configs.
If changes are necessary, consider contributing them back ;)

For more complex projects, it might be feasible to use a custom build-config file
that just `import()s` [`//build/config/BUILDCONFIG.gn`](config/BUILDCONFIG.gn) and then overrides
the defaults set inside `BUILDCONFIG.gn`. There's also GN's `default_args` scope, which can be used
to provide project-specific argument overrides.
