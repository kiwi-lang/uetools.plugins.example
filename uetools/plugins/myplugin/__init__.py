"""Top level module for uetools_plugin"""

__descr__ = "uetools plugin example"
__version__ = "version"
__license__ = "BSD 3-Clause License"
__author__ = "Pierre Delaunay"
__author_email__ = "pierre@delaunay.io"
__copyright__ = "2022 Pierre Delaunay"
__url__ = "https://github.com/kiwi-lang/uetools_plugin"


from .command import MyNewCommand

# Register the commands here
COMMANDS = [
    MyNewCommand,
]
