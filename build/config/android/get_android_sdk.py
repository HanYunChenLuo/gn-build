import sys
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
    str = exe_command("echo $HOME")
    if sys.platform == 'darwin':
        str += '/Library/Android/sdk'
    elif sys.platform == 'linux':
        str += '/Android/Sdk'
    else:
         raise Exception("This script only runs on Mac and Linux")
    print (str)
    return 0

if __name__ == '__main__':
  sys.exit(main())