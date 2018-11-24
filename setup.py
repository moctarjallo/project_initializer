import setuptools
import os
import sys


PROJECT_NAME = "project_initializer"
DATA_DIR = os.path.join(
    sys.prefix, "local/lib/python3.6/dist-packages", PROJECT_NAME)


setuptools.setup(
    name='project_initializer',
    version='0.1.0',
    packages=setuptools.find_packages(),
    package_dir={'project_initializer': 'project_initializer'},
    package_data={'project_initializer': [
        'data/README.md', 'data/.gitignore']},
    install_requires=[
        'docopt'
    ],
    entry_points={
        'console_scripts': [
            'proj = project_initializer.__main__:main'
        ]
    }
)
