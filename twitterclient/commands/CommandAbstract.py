from twitterclient.helpers import Config


class CommandAbstract(object):
    # the general configs for the application
    general_config = Config().load('general')

    # the user configs
    user_config = Config().load('user')

    def __init__(self, view, twitter):
        self.view = view
        self.twitter = twitter

    def is_valid_session(self):
        if self.twitter.api is None:
            self.view.update_status_area("You need to be logged in to run this command")
            return False

        return True

    def run(self):
        raise NotImplementedError()