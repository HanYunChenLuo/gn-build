import os
import sys
from optparse import OptionParser

sys.path.insert(1, os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
import gn_helpers

def get_ndk_root():
    parser = OptionParser()
    parser.add_option("--ndk-version",
                      action="store_true", dest="ndk-version", default='',
                      help="Additionally print the ndk-version (appears first).")
    options, args = parser.parse_args()
    # ndk_version = ''
    if len(args) == 1:
        ndk_version = args[0]
    ndk_path = os.environ['HOME']
    if sys.platform == 'darwin':
        ndk_path += '/Library/Android/sdk/ndk/'
    elif sys.platform == 'linux':
        ndk_path += '/Android/Sdk/ndk/'
    else:
         raise Exception("This script only runs on Mac and Linux")
    filelist = os.listdir(ndk_path)
    filelist.sort()

    ndk_valid = False
    ndk_max_exsit_version = ''
    for i in filelist:
        ndk_build_exe = ndk_path + i + '/ndk-build'
        if(os.access(ndk_build_exe, mode=os.X_OK)):
            ndk_max_exsit_version = i
            if(i == ndk_version and ndk_version != ''):
                break

    if (ndk_max_exsit_version == ''):
        raise Exception("Could not find valid NDK!")

    if (ndk_version != ''):
        num_ndk_max_exsit_version = int(ndk_max_exsit_version.replace('.', ''))
        num_ndk_version = int(ndk_version.replace('.', ''))

        if (num_ndk_max_exsit_version < num_ndk_version):
            raise Exception("Existed NDK is too older, please download newest NDK!")

    ndk_path += ndk_max_exsit_version
    return ndk_path


def main():
    ndk_path = get_ndk_root()
    sys.stdout.write(
        gn_helpers.ToGNString({
            'ndk_root': ndk_path,
        }))
    return 0

if __name__ == '__main__':
  sys.exit(main())