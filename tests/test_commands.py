import unittest
import os
from nose.tools import raises
from mock import patch, MagicMock, PropertyMock

from twitterclient.commands.CommandList import CommandList
from twitterclient.commands.CommandExit import CommandExit
from twitterclient.commands.CommandLogout import CommandLogout


class View:
    def update_status_area(self):
        pass


class Twitter:
    api = None


class CommandsTest(unittest.TestCase):

    def setUp(self):
        self.view = View()
        self.view.update_status_area = MagicMock(name='update_status_area')
        self.twitter = Twitter()

        self.test_user_config = os.path.join(os.path.dirname(__file__), '.test_user_config')

    @raises(SystemExit)
    def test_exit(self):
        CommandExit(self.view, self.twitter).run()

    def test_logout_config_file_exists(self):
        with patch('twitterclient.helpers.Config.user_config_file', new_callable=PropertyMock) as user_config_file:
            user_config_file.return_value = self.test_user_config

            #create the config file
            open(self.test_user_config, 'a').close()

            CommandLogout(self.view, self.twitter).run()
            self.view.update_status_area.assert_called_once_with(
                "Successfully logged you out"
            )

    def test_logout_config_file_missing(self):
        CommandLogout(self.view, self.twitter).run()
        self.view.update_status_area.assert_called_once_with(
            "Could not log you out. Please try again"
        )

    def test_list_no_session(self):
        self.assertFalse(CommandList(self.view, self.twitter).run())

    def test_list_no_session(self):
        self.assertFalse(CommandList(self.view, self.twitter).run())

    def tearDown(self):
        try:
            os.remove(self.test_user_config)
        except OSError:
            pass
