import tweepy
from ConfigParser import NoSectionError
from view import View
from helpers import Config
from commands.CommandFactory import get_command


class Controller():
    # the view class
    view = None

    # the config data for the logged in Twitter user
    user_config = Config().load('user')

    # the general configs for the application
    general_config = Config().load('general')

    # the Twitter auth token, if needed
    twitter_auth = None

    # The API handler for twitter
    api = None

    def __init__(self):
        self.init_view()
        self.init_command_listener()

    def init_view(self):
        """
        Initiate the view and prints out the main screen
        """
        self.init_twitter_auth()

        self.view = View()
        self.view.print_intro(self.get_status())
        self.view.update_status_area("Please input a command")

    def init_command_listener(self):
        """
        Listen for a command from the user and runs it once it has been inputted
        """
        while True:  # keep the program alive
            command = self.view.get_input("What would you like to do: ")
            self.run_command(command)

    def init_twitter_auth(self):
        self.twitter_auth = tweepy.OAuthHandler(
            self.general_config.get('Twitter', 'consumer_token'),
            self.general_config.get('Twitter', 'consumer_secret')
        )

        self.init_twitter_user()

    def init_twitter_user(self):
        try:
            self.twitter_auth.set_access_token(
                self.user_config.get('Client', 'client_consumer_token'),
                self.user_config.get('Client', 'client_consumer_secret')
            )
        except NoSectionError:
            return False
        else:
            self.api = tweepy.API(self.twitter_auth)

    def run_command(self, command):
        """
        Listen for a command from the user and runs it once it has been inputted
        """
        try:
            cls = get_command(command)
        except ValueError:
            self.view.update_status_area("I'm afraid you can't do %s" % command)
        else:
            cls(self.view, self.twitter_auth).run()

    def get_status(self):
        """
        Get the status of the user as a string: Logged in as/Not logged in
        If the user is not logged in, the self.api property will be None
         raising an Attribute error when called
        If the user is logged in, but the credentials are rejected,
         tweepy will raise a TweepError
        """
        try:
            current_user = self.api.me()
        except (AttributeError, tweepy.TweepError):
            return "Not logged in"
        else:
            return "You are logged in as %s" % current_user.screen_name