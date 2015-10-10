import os
from CommandAbstract import CommandAbstract
from twitterclient.helpers import Config


class CommandLogout(CommandAbstract):
    def run(self):
        if not self.is_valid_session():
            return False

        try:
            os.remove(Config.user_config_file)
        except OSError:
            self.view.update_status_area("Could not log you out. Please try again")
        else:
            self.view.update_status_area("Successfully logged you out")
            self.view.print_intro("Not logged in")
