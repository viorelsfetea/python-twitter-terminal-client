from CommandAbstract import CommandAbstract


class CommandHelp(CommandAbstract):
    def run(self):
        self.view.print_intro(self.twitter.get_status())