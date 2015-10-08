from twitterclient.view import View
from twitterclient.commands.CommandFactory import get_command
from twitterclient.twitter import Twitter


class Controller():
    # the view class
    view = None

    # the Twitter handler
    twitter = Twitter()

    # The API handler for twitter
    api = None

    def __init__(self):
        self.init_view()
        self.init_command_listener()

    def init_view(self):
        """
        Initiate the view and prints out the main screen
        """
        self.view = View()
        self.view.print_intro(self.twitter.get_status())
        self.view.update_status_area("Please input a command")

    def init_command_listener(self):
        """
        Listen for a command from the user and runs it once it has been inputted
        """
        while True:  # keep the program alive
            command = self.view.get_input("What would you like to do: ")
            self.run_command(command)

    def run_command(self, command):
        """
        Listen for a command from the user and runs it once it has been inputted
        """
        try:
            cls = get_command(command)
        except ValueError:
            self.view.update_status_area("I'm afraid you can't do %s" % command)
        else:
            cls(self.view, self.twitter).run()
