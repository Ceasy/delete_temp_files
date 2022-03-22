import getpass
import os

from cx_Freeze import *
from os.path import abspath


USER_NAME = getpass.getuser()


def setup():
    setup(
        executable = [
            Executable(
                "test.py",
                shortcutName="Testing",
                shortcutDir="MSI"
                # shortcutDir="c:/Users/1/Desktop/"
            )
        ]
    )

def main():
    bat_path = r'C:\Users\%s\Downloads\777' % USER_NAME
    print(bat_path)


if __name__ == '__main__':
    # main()