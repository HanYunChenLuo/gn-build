from distutils.command.build import build
import os
import sys
from optparse import OptionParser

sys.path.insert(1, os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
import gn_helpers

def getSDKRoot(sdk_version):
    if(sdk_version == ''):
        return ''

    sdk_root = os.environ['HOME']
    if sys.platform == 'darwin':
        sdk_root += '/Library/Android/sdk/platforms/android-' + sdk_version
    elif sys.platform == 'linux':
        sdk_root += '/Android/Sdk/platforms/android-' + sdk_version
    else:
         raise Exception("This script only runs on Mac and Linux")
    if(os.access(sdk_root, mode=os.F_OK)):
        return sdk_root
    else:
        return ''

def getBuildToolsRoot(build_tools):
    if(build_tools == ''):
        return ''

    sdk_root = os.environ['HOME']
    if sys.platform == 'darwin':
        sdk_root += '/Library/Android/sdk'
    elif sys.platform == 'linux':
        sdk_root += '/Android/Sdk'
    else:
         raise Exception("This script only runs on Mac and Linux")
    return sdk_root

def main():
    parser = OptionParser()
    parser.add_option("--sdk-version",
                      action="store", dest="sdk_version", default='',
                      help="Additionally print the ndk-version (appears first).")
    parser.add_option("--build-tools-version",
                      action="store", dest="build_tools_version", default='',
                      help="Additionally print the build-tools-version (appears first).")
    options, args = parser.parse_args()
    sdk_version = options.sdk_version
    build_tools_version = options.build_tools_version

    sdk_root = getSDKRoot(sdk_version)
    build_tools_root = getSDKRoot(build_tools_version)
    sys.stdout.write(
        gn_helpers.ToGNString({
            'sdk_root': sdk_root,
        }))
    return 0

if __name__ == '__main__':
  sys.exit(main())