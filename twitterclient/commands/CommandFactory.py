from CommandAbstract import CommandAbstract
from CommandExit import CommandExit
from CommandLogin import CommandLogin
from CommandHelp import CommandHelp
from CommandList import CommandList
from CommandLogin import CommandLogin
from CommandLogout import CommandLogout
from CommandPost import CommandPost
from CommandNext import CommandNext
from CommandPrev import CommandPrev


def get_command(command):
    for cls in CommandAbstract.__subclasses__():
        if cls.__name__ == 'Command%s' % command.capitalize():
            return cls

    raise ValueError
