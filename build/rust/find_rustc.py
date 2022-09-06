import subprocess
import sys
from subprocess import Popen, PIPE, STDOUT


def exe_command(command):
    """
    执行 shell 命令并实时打印输出
    :param command: shell 命令
    :return: process, exitcode
    """
    result = ""
    process = Popen(command, stdout=PIPE, stderr=STDOUT, shell=True)
    with process.stdout:
        for line in iter(process.stdout.readline, b''):
            result += line.decode().strip()
    exitcode = process.wait()
    return result

def main():
    str= exe_command("which rustc")
    str1 = str.replace('/bin/rustc', '')
    print(str1)

if __name__ == '__main__':
  sys.exit(main())