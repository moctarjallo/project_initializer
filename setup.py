import setuptools

setuptools.setup(
    name='project_initializer',
    version='0.1.0',
    packages=setuptools.find_packages(),
    install_requires=[
        'docopt'
    ],
    entry_points={
        'console_scripts': [
            'proj = project_initializer.__main__:main'
        ]
    }
)
