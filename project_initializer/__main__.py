"""project initializer
Usage:
    proj init <project>

"""


from docopt import docopt

from . import init


def main():
    args = docopt(__doc__)
    if args['init']:
        init.run(args['<project>'])
