import unittest
import os
from nose.tools import raises
from mock import patch, MagicMock, PropertyMock

from twitterclient.commands.CommandList import CommandList
from twitterclient.commands.CommandExit import CommandExit
from twitterclient.commands.CommandLogout import CommandLogout
from twitterclient.commands.CommandNext import CommandNext
from twitterclient.commands.CommandPrev import CommandPrev
from twitterclient.commands.CommandHelp import CommandHelp


class View:
    def update_status_area(self):
        pass

    def print_intro(self):
        pass

class Twitter:
    api = None
    page = 1

    def get_status(self):
        pass


class CommandsTest(unittest.TestCase):

    def setUp(self):
        self.view = View()
        self.view.update_status_area = MagicMock(name='update_status_area')
        self.view.print_intro = MagicMock(name='print_intro')
        self.twitter = Twitter()

        self.test_user_config = os.path.join(os.path.dirname(__file__), '.test_user_config')

    @raises(SystemExit)
    def test_exit(self):
        CommandExit(self.view, self.twitter).run()

    def test_help(self):
        CommandHelp(self.view, self.twitter).run()

        self.view.print_intro.assert_called_once_with(None)

    def test_logout_config_file_exists(self):

        with patch('twitterclient.helpers.Config.user_config_file', new_callable=PropertyMock) as user_config_file:
            self.twitter.api = object

            user_config_file.return_value = self.test_user_config

            # create the config file
            open(self.test_user_config, 'a').close()

            CommandLogout(self.view, self.twitter).run()
            self.view.update_status_area.assert_called_once_with(
                "Successfully logged you out"
            )

    def test_logout_config_file_missing(self):
        with patch('twitterclient.helpers.Config.user_config_file', new_callable=PropertyMock) as user_config_file:
            self.twitter.api = object

            user_config_file.return_value = self.test_user_config

            CommandLogout(self.view, self.twitter).run()
            self.view.update_status_area.assert_called_once_with(
                "Could not log you out. Please try again"
            )

    def test_list_no_session(self):
        self.assertFalse(CommandList(self.view, self.twitter).run())

    @patch("twitterclient.commands.CommandList.CommandList.run")
    def test_next(self, super_run):
        CommandNext(self.view, self.twitter).run()

        self.assertEquals(2, self.twitter.page)

        self.assertTrue(super_run.called)

    @patch("twitterclient.commands.CommandList.CommandList.run")
    def test_prev_first_page(self, super_run):
        CommandPrev(self.view, self.twitter).run()

        self.view.update_status_area.assert_called_once_with(
            "You are already on the first page"
        )

    @patch("twitterclient.commands.CommandList.CommandList.run")
    def test_prev(self, super_run):

        self.twitter.page = 5

        CommandPrev(self.view, self.twitter).run()

        self.assertEquals(4, self.twitter.page)

        self.assertTrue(super_run.called)

    def tearDown(self):

        self.twitter.page = 1

        try:
            os.remove(self.test_user_config)
        except OSError:
            pass
