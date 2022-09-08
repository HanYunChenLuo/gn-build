import sys
from optparse import OptionParser
import subprocess

def exe_command(command):
    """
    执行 shell 命令并实时打印输出
    :param command: shell 命令
    :return: process, exitcode
    """
    result = ""
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    with process.stdout:
        for line in iter(process.stdout.readline, b''):
            result += line.decode().strip()
    exitcode = process.wait()
    return result

def main():
    parser = OptionParser()
    parser.add_option("--ndk-version",
                      action="store_true", dest="ndk-version", default=False,
                      help="Additionally print the ndk-version (appears first).")
    options, args = parser.parse_args()
    if len(args) != 1:
      parser.error('Please specify a minimum SDK version')
    ndk_version = args[0]
    str = exe_command("echo $HOME")
    if sys.platform == 'darwin':
        str += '/Library/Android/sdk/ndk/' + ndk_version
    elif sys.platform == 'linux':
        str += '/Android/Sdk/ndk/'+ ndk_version
    else:
         raise Exception("This script only runs on Mac and Linux")
    print (str)
    return 0

if __name__ == '__main__':
  sys.exit(main())