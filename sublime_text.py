#!/usr/bin/env python

from os import getcwd, getenv
from os.path import join, expanduser, realpath
from sys import argv, exit, dont_write_bytecode
from subprocess import call


UNIX_C = getenv("UNIX_C", "/mnt/c")
UNIX_HOME = getenv("UNIX_HOME", "/home/michaelhollister")
WINDOWS_C = getenv("WINDOWS_C", "C:\\")
WINDOWS_HOME = getenv("WINDOWS_HOME", "%sUsers/Mike" % WINDOWS_C)
SUBLIME_TEXT_UNIX = getenv("SUBLIME_TEXT_UNIX", "%s/Program\ Files/Sublime\ Text\ 3/subl.exe" % UNIX_C)


def HOME():
    return expanduser("~")


def get_fullpath(file):
    file = realpath(file)
    if file[0] == "/":
        # assuming script fullpath
        pass
    else:  # relative path
        if file[0] == "~" and len(file) == 1:  # "~"
            file = HOME()
        elif file[0] == "." and len(file) == 1:  # "."
            file = getcwd()
        elif file[0] + file[1] == "~/":  # "~/$file"
            file = join(HOME(), "/", file[2:])

        elif file[0] + file[1] == "./":  # "./$file"
            file = join(getcwd(), file[2:])
        else:
            file = join(getcwd(), file)
    return file


def wsl_convert(file_fullpath, to_windows=True):
    if to_windows:
        if UNIX_HOME in file_fullpath:
            return file_fullpath.replace(UNIX_HOME, WINDOWS_HOME)
        else:
            return file_fullpath.replace(UNIX_C, WINDOWS_C)
    else:
        if WINDOWS_HOME in file_fullpath:
            return file_fullpath.replace(WINDOWS_HOME, UNIX_HOME)
        else:
            return file_fullpath.replace(WINDOWS_C, UNIX_C)


def open_in_sublime_text(file):
    return call("%s %s" % (SUBLIME_TEXT_UNIX, file), shell=True) 


if __name__ == '__main__':
    if len(argv) < 2:
        print("Need a filename")
        exit(1)
    else:
        for file in argv:
            if file != argv[0]:
                file = get_fullpath(file)
                file = wsl_convert(file)
                open_in_sublime_text(file)
        exit(0)

