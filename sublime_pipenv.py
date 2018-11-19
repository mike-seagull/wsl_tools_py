#!/usr/bin/python -B

# from imp import load_source
from sys import argv, stdout
from subprocess import Popen, PIPE, STDOUT
# st = load_source("sublime_text", "/home/michaelhollister/repos/.bin/sublime_text")
import sublime_text as st

def execute(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT)

    # Poll process for new output until finished
    while True:
        nextline = p.stdout.readline()
        if nextline == '' and p.poll() is not None:
            break
        stdout.write(nextline)
        stdout.flush()

    output = p.communicate()[0]
    rc = p.returncode

    if (rc == 0):
        return output
    else:
        print("Error: Failed to run %s" % output)


def get_pipenv_binary(project_dir):
    p = Popen("/usr/local/bin/pipenv --py", stdout=PIPE, shell=True, cwd=project_dir)
    pipenv_binary, err = p.communicate()
    if err:
        print(err)
    return pipenv_binary


if __name__ == '__main__':
    file = argv[1]
    project_dir = argv[2]
    file = st.get_fullpath(file)
    file = st.wsl_convert(file, False)  # convert to unix
    project_dir = st.get_fullpath(project_dir)
    project_dir = st.wsl_convert(project_dir, False)  # convert to unix
    pipenv_binary = get_pipenv_binary(project_dir)
    execute("%s %s" % (pipenv_binary, file))
