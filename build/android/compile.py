import sys
import os
import shutil
import argparse
import subprocess

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--path', type=str)
  args = parser.parse_args()
  app_dir = args.path.split("//")[1]
  print(app_dir)
  build_root = os.getcwd()
  root = build_root.split("out")[0]
  app_root_dir = root + app_dir
  print(build_root)
  os.chdir(app_root_dir)
  subprocess.run("cargo ndk -t arm64-v8a -o app/src/main/jniLibs build", shell=True)
  subprocess.run("./gradlew build", shell=True)
  shutil.copyfile(app_root_dir + "/target/aarch64-linux-android/debug/libmain.so", build_root + "/libmain.so")
  shutil.copyfile(app_root_dir + "/app/build/outputs/apk/debug/app-debug.apk", build_root + "app-debug.apk")
  return app_root_dir


if __name__ == '__main__':
  print(main())
  sys.exit(0)
