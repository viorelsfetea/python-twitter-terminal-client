import tweepy
from ConfigParser import NoSectionError
from twitterclient.helpers import Config


class Twitter(object):
    # The auth handler, used to log in the user
    twitter_auth = None

    # The api handler, if the user is logged in
    api = None

    def __init__(self):
        self.load_auth_handler()
        self.load_api_handler()

    def load_auth_handler(self):
        """
        Load the Twitter Auth handler
        """
        self.twitter_auth = tweepy.OAuthHandler(
            Config().load('general').get('Twitter', 'consumer_token'),
            Config().load('general').get('Twitter', 'consumer_secret')
        )

    def load_api_handler(self):
        """
        Load the Twitter API handler
        """
        try:
            self.twitter_auth.set_access_token(
                Config().load('user').get('Client', 'client_consumer_token'),
                Config().load('user').get('Client', 'client_consumer_secret')
            )
        except NoSectionError:
            return None
        else:
            self.api = tweepy.API(self.twitter_auth)

    def get_status(self):
        """
        Get the status of the user as a string: Logged in as/Not logged in
        If the user is not logged in, the self.api property will be None
         raising an Attribute error when called
        If the user is logged in, but the credentials are rejected,
         tweepy will raise a TweepError
        """
        try:
            current_user = self.get_user()
        except (AttributeError, tweepy.TweepError):
            return "Not logged in"
        else:
            return "You are logged in as %s" % current_user.screen_name

    def get_user(self):
        """
        Get the current logged in user
        :return: object
        """
        return self.api.me()
