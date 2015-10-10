import curses
from CommandAbstract import CommandAbstract


class CommandList(CommandAbstract):
    # The lists of tweets to be loaded
    tweets = []

    # the total number of tweets to retrieve
    total_tweets = 30

    # The pattern to print the tweets
    tweet_line = '{0:<2} | {1:<16} | {2:<16} | {3:<141}'

    HEADER_PADDING = 2

    def run(self):

        if not self.is_valid_session():
            return False

        self.get_and_print_tweets()

    def get_and_print_tweets(self):
        self.tweets = self.twitter.api.home_timeline(count=self.total_tweets, page=self.twitter.page)
        self.show_tweets_screen()

    def draw_separator_bar(self, top):
        self.view.screen.addstr(top, 0, '=' * (self.view.screen.getmaxyx()[1] - 5))

    def show_tweets_screen(self):
        self.view.screen.clear()

        self.build_list_header()
        self.build_list_content()
        self.build_list_footer()

        self.view.screen.refresh()

    def build_list_content(self):
        for tweet_index, tweet in enumerate(self.tweets, start=1):

            tweet_string = self.tweet_line.format(
                self.get_index_representation(tweet_index),
                tweet.author.screen_name,
                tweet.created_at.strftime("%A, %I:%M"),
                tweet.text.encode("utf_8").replace("\n", " ")
            )

            self.view.screen.addstr(tweet_index + self.HEADER_PADDING, 0, tweet_string, curses.A_NORMAL)

    @staticmethod
    def get_index_representation(tweet_index):
        if tweet_index < 10:
            return '0%d' % tweet_index

        return tweet_index

    def build_list_header(self):
        result_header = self.tweet_line.format('#', 'Who', 'When', 'What')
        self.view.screen.addstr(self.HEADER_PADDING - 1, 0, result_header)

        self.draw_separator_bar(self.HEADER_PADDING)

    def build_list_footer(self):
         self.draw_separator_bar(self.HEADER_PADDING + len(self.tweets))