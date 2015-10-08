from CommandAbstract import CommandAbstract
import tweepy
import webbrowser

from ..helpers import Config


class CommandLogin(CommandAbstract):
    def run(self):
        self.open_twitter_auth_screen()

    def open_twitter_auth_screen(self):
        """
        Opens a browser window to show the authorization PIN to the user
        """
        try:    
            webbrowser.open(self.twitter.twitter_auth.get_authorization_url())
        except tweepy.TweepError:
            self.view.update_status_area('Error! Failed to get request token.')
        else:
            self.get_twitter_access_token()

    def get_twitter_access_token(self):
        """
        Creates a listener for the PIN user input
        """
        pin = self.view.get_input('PIN from the browser: ')

        self.save_twitter_access_token(pin)

    def save_twitter_access_token(self, pin):
        """
        Saves the access token generated based on the PIN entered by the user
        :param pin:
        """
        try:
            consumer_token, consumer_secret = self.twitter.twitter_auth.get_access_token(pin)
        except tweepy.error.TweepError:
            self.view.update_status_area('Failed to get request token. Please try again')
        else:
            Config().save({
                'client_consumer_token': consumer_token,
                'client_consumer_secret': consumer_secret
            }, 'Client')

            self.finish_login()

    def finish_login(self):
        self.twitter.load_api_handler()

        user = self.twitter.get_user()

        self.view.print_intro("You are logged in as %s" % user.screen_name)
        self.view.update_status_area('Successfully logged in. Input your command')