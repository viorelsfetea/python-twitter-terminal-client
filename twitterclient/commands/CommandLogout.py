import os
from CommandAbstract import CommandAbstract
from ..helpers import Config


class CommandLogout(CommandAbstract):
    def run(self):
        try:
            os.remove(Config.user_config_file)
        except OSError:
            self.view.update_status_area("Could not log you out. Please try again")
        else:
            self.view.update_status_area("Successfully logged you out")
