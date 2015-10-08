import sys
import unittest
from mock import Mock
from nose.tools import raises

# simply importing the curses module transforms the terminal
# into a curses screen messing up all of the output
# this mocks the curses module
sys.modules['curses'] = Mock()

from twitterclient.controller import Controller


#class ControllerTest(unittest.TestCase):
    #controller = Controller()