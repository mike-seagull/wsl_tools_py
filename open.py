#!/usr/bin/python -B

from imp import load_source
from sys import argv, exit
from subprocess import check_call, CalledProcessError
# st = load_source("sublime_text", "/home/michaelhollister/repos/.bin/sublime_text")
import sublime_text as st

def open(file):
    try:
        check_call("cmd.exe /c start %s" % file, shell=True)
    except CalledProcessError:
        raise


if __name__ == '__main__':
    try:
        file = argv[1]
        file = st.get_fullpath(file)
        if st.UNIX_C not in file:
            raise Exception("Cannot open")
        else:
            file = st.wsl_convert(file)
            open(file)
            exit(0)
    except (CalledProcessError, Exception):
        print "Error: Cannot open %s" % file
        exit(1)
