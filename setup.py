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
    install_requires=[
        'docopt'
    ],
    data_files=[
        (DATA_DIR, [
            "README.md",
            ".gitignore"
        ])
    ],
    entry_points={
        'console_scripts': [
            'proj = project_initializer.__main__:main'
        ]
    }
)
