import curses
from CommandAbstract import CommandAbstract


class CommandList(CommandAbstract):

    # The lists of tweets to be loaded
    tweets = []

    def run(self):
        self.require_valid_session()

        self.show_tweets_screen(
            self.twitter.api.home_timeline()
        )

    def show_tweets_screen(self, tweets):
        self.view.screen.clear()

        result_line = '{0:<2} | {1:<16} | {2:<16} | {3:<141}'
        result_header = result_line.format('#', 'Who', 'When', 'What')
        separator_bar = '=' * (self.view.screen.getmaxyx()[1] - 5)

        self.view.screen.addstr(1, 0, result_header)
        self.view.screen.addstr(2, 0, separator_bar)

        for tweet_index, tweet in enumerate(tweets, start=1):
            if len(str(tweet_index)) == 1:
                tweet_index_str = '0' + str(tweet_index)
            else:
                tweet_index_str = str(tweet_index)

            tweet_text = tweet.text.encode("utf_8").replace("\n", " ")
            track_string = result_line.format(tweet_index_str, tweet.author.screen_name, tweet.created_at.strftime("%A, %I:%M"), tweet_text)
            self.view.screen.addstr(tweet_index + 2, 0, track_string, curses.A_NORMAL)

        bottom_bar_position = 2 + len(self.tweets)
        self.view.screen.addstr(bottom_bar_position, 0, separator_bar)
        self.view.screen.refresh()
