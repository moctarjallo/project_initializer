import subprocess
import os
import shutil

"""Create a new project and initialize it with a .gitignore file
@params project: name of a project to be initialized
effects:
    /project
        .gitignore
    .gitignore in the created project directory must be the same as the gitignore in THIS directory 
"""


def run(project):
    os.mkdir(project)
    os.chdir(project)
    shutil.copyfile('.gitignore', '.')  # problem


if __name__ == '__main__':
    run("hello-world")
