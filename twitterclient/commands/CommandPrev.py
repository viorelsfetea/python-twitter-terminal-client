from CommandAbstract import CommandAbstract
from CommandList import CommandList


class CommandPrev(CommandList, CommandAbstract):
    def run(self):
        if self.twitter.page > 1:
            self.twitter.page -= 1
            super(CommandPrev, self).run()
        else:
            self.view.update_status_area("You are already on the first page")