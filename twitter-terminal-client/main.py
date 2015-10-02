import curses

from client import TwitterClient


class TwitterClientInterface(object):

    # The app's screen
    screen = curses.initscr()

    # The Twitter library
    client = TwitterClient()

    # The area that will show the current status
    status_area = False

    # The area that will show any prompt text for the user
    prompt_area = False

    # The area that will show the input for the user
    input_prompt = False

    # The area that will receive the input for the user
    search_window = False

    # The curent status
    status = "Please input a command"

    def __init__(self):
        self.init_interface()
        self.print_intro()
        self.update_status_area()
        self.init_command_listener()

    def draw_screen_areas(self):
        '''
        +--------------------------------------------------+
        |                                                  |
        |                                                  |
        |                                                  |
        |                     Main area                    |
        |                                                  |
        |                                                  |
        +--------------------------------------------------+
        | Prompt area/Input prompt                         |
        |                                                  |
        +--------------------------------------------------+
        | Status area                                      |
        |                                                  |
        +--------------------------------------------------+
        '''

        self.status_area = self.screen.subwin(33, 120, 0, 0)
        begin_y = self.status_area.getmaxyx()[0]

        # build everything else relative to the status area
        self.prompt_area = self.screen.subwin(5, 120, begin_y, 0)
        self.input_prompt = self.screen.subwin(1, 29, begin_y, 1)
        self.search_window = self.screen.subwin(1, 100, begin_y, 28)

    def init_interface(self):
        curses.curs_set(0)
        curses.noecho()

        self.draw_screen_areas()

    def init_command_listener(self):
        command = self.get_input("What would you like to do: ")

    def update_main_screen(self, content):
        self.screen.clear()
        self.screen.addstr(0, 0, content)
        self.screen.refresh()

    def update_status_area(self):
        self.status_area.addstr(0, 0, self.status)
        self.status_area.refresh()

    def print_intro(self):
        intro_text = '''
                     _____         _     _____        _ _   _                   _ _            _
                    |_   _|       | |   |_   _|      (_) | | |                 | (_)          | |
                      | | ___  ___| |_    | |_      ___| |_| |_ ___ _ __    ___| |_  ___ _ __ | |_
                      | |/ _ \/ __| __|   | \ \ /\ / / | __| __/ _ \ '__|  / __| | |/ _ \ '_ \| __|
                      | |  __/\__ \ |_    | |\ V  V /| | |_| ||  __/ |    | (__| | |  __/ | | | |_
                      \_/\___||___/\__|   \_/ \_/\_/ |_|\__|\__\___|_|     \___|_|_|\___|_| |_|\__|

                    '''

        intro_text += "Status: %s" % self.client.get_status()

        self.update_main_screen(intro_text)

    def get_input(self, prompt):
        """Get user input through the user interface and return it."""
        curses.curs_set(2)

        self.prompt_area.clear()
        self.input_prompt.addstr(0, 0, prompt)
        self.search_window.clear()
        self.prompt_area.refresh()

        curses.echo()
        user_input = self.search_window.getstr().decode(encoding="utf-8")
        curses.noecho()

        self.prompt_area.clear()
        self.prompt_area.refresh()

        curses.curs_set(0)
        return user_input

if __name__ == '__main__':
    TwitterClientInterface()