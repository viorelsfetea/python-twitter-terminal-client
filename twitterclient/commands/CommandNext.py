from CommandAbstract import CommandAbstract
from CommandList import CommandList


class CommandNext(CommandList, CommandAbstract):
    def run(self):
        self.twitter.page += 1
        super(CommandNext, self).run()