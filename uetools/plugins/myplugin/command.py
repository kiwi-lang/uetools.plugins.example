"""My new command"""
from dataclasses import dataclass

from simple_parsing import choice
from uetools.command import Command, command_builder, newparser
from uetools.conf import editor_cmd, find_project, uat
from uetools.format.base import Formatter
from uetools.run import popen_with_format


@dataclass
class Arguments:
    """Arguments for my new command"""

    project: str
    flag: bool = False
    value: str = ""
    choice: str = choice("a", "b", "c", type=str, default="a")


class MyNewCommand(Command):
    """My new command does this"""

    name: str = "command"

    @staticmethod
    def arguments(subparsers):
        """Add arguments to the parser"""
        parser = newparser(subparsers, MyNewCommand)
        parser.add_arguments(Arguments, dest="args")

    @staticmethod
    def execute(args):
        """Execute the command"""
        cmd = command_builder(args)

        uproject = find_project(args.args.project)

        fmt = Formatter()
        popen_with_format(fmt, [uat(), uproject] + cmd)

        popen_with_format(fmt, [editor_cmd()] + cmd)
