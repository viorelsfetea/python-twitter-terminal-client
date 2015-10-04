import sys
import webbrowser

from view import View


class Controller():
    # the view class
    view = False

    # a dict containing all the commands
    commands = {}

    def init_view(self):
        """
        Initiate the view and prints out the main screen
        """
        self.view = View()
        self.view.print_intro(self.get_status())
        self.view.update_status_area("Please input a command")

    def set_available_commands(self):
        """
        Maps out the commands that are available to users
        """
        self.commands = {
            'login': self.do_login,
            'exit': self.do_exit,
            'list': self.do_list
        }

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
            self.commands[command]()
        except KeyError:
            self.view.update_status_area("I'm afraid you can't do %s" % command)

    def get_status(self):
        """
        Get the status of the user as a string: Logged in as/Not logged in
        """
        return "Not logged in"

    def do_login(self):
        webbrowser.open("http://google.com")

    def do_list(self):
        pass

    @staticmethod
    def do_exit():
        sys.exit(1)