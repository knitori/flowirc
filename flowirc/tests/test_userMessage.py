from unittest import TestCase
from flowirc.messages import UserMessage


__author__ = 'olle.lundberg'


class TestUserMessage(TestCase):
    def test_usermessage(self):
        self.assertEqual("USER bar 0 * :baz\r\n",
                         str(UserMessage("bar", "baz")))