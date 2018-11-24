import subprocess
import os
import shutil
import sys

"""Create a new project and initialize it with a .gitignore file
@params project: name of a project to be initialized
effects:
    /project
        .gitignore
    .gitignore in the created project directory must be the same as the gitignore in THIS directory 
"""

PROJECT_NAME = "project_initializer"
DATA_DIR = os.path.join(
    sys.prefix, "local/lib/python3.6/dist-packages", PROJECT_NAME)


def run(project):
    os.mkdir(project)
    shutil.copyfile(os.path.join(DATA_DIR, "README.md"),
                    f"{project}/README.md")  # problem


if __name__ == '__main__':
    run("hello-world")
