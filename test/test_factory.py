import unittest
from twitterclient.commands.CommandFactory import get_command
from twitterclient.commands.CommandExit import CommandExit


class FactoryTest(unittest.TestCase):

    def test_get_command(self):
        cls = get_command('exit')
        self.assertEquals(CommandExit, cls)