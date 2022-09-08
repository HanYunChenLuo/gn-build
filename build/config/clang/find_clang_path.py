import sys
import os
from optparse import OptionParser
import subprocess
import platform

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
    str = ''
    if sys.platform == 'darwin':
        if(platform.processor() == 'arm'):
            str += '/opt/homebrew/Cellar/llvm/'
        else:
            str += '/usr/local/homebrew/Cellar/llvm'
        list_result = os.listdir(str)
        str += list_result[0]
    elif sys.platform == 'linux':
        str += '/usr'
    else:
         raise Exception("This script only runs on Mac and Linux")
    print (str)
    return 0

if __name__ == '__main__':
  sys.exit(main())