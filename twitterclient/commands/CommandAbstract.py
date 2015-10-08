import tweepy
from helpers import Config


class CommandAbstract(object):
    # the general configs for the application
    general_config = Config().load('general')

    # the user configs
    user_config = Config().load('user')

    def __init__(self, view, twitter_auth):
        self.view = view
        self.twitter_auth = twitter_auth

    def run(self):
        raise NotImplementedError()