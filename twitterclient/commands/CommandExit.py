import sys
from CommandAbstract import CommandAbstract


class CommandExit(CommandAbstract):
    def run(self):
        sys.exit()
