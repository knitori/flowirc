from unittest import TestCase
from flowirc.messages import ModeMessageBase


__author__ = 'olle.lundberg'


class TestModeMessageBase(TestCase):
    def test_modemessagebase(self):
        self.assertEqual("MODE channel +o bla\r\n",
                         str(ModeMessageBase("channel", "+o", "bla")))