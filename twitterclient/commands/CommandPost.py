import tweepy
from CommandAbstract import CommandAbstract


class CommandPost(CommandAbstract):
    post = None

    def run(self):
        self.get_post_from_user()

    def get_post_from_user(self):
        """
        Create a listener for the post user input
        """
        self.post = self.view.get_input('Your post (max 140 chars): ')

        self.save_post()

    def save_post(self):
        """
        Save the post to Twitter
        """
        if self.post_is_valid():
            try:
                self.twitter.api.update_status(status=self.post)
            except tweepy.error.TweepError:
                self.view.update_status_area('Failed to update your status')
            else:
                self.view.update_status_area('Successfully updated your status')

    def post_is_valid(self):
        """
        Check if the inputted post is shorter than 140
        :return: bool
        """
        if self.post is not None and len(self.post) <= 140:
            return True

        return False
