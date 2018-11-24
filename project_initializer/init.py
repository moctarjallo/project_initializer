import subprocess
import os
import shutil
import sys

from . import PROJECT_DIR

"""Create a new project and initialize it with a .gitignore file
@params project: name of a project to be initialized
effects:
    /project
        .gitignore
    .gitignore in the created project directory must be the same as the gitignore in THIS directory 
"""


def run(project):
    os.mkdir(project)
    shutil.copyfile(os.path.join(PROJECT_DIR, 'data/README.md'),
                    f"{project}/README.md")  # problem


if __name__ == '__main__':
    run("hello-world")
