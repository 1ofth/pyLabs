from unittest import TestCase
from string2 import *


class Test(TestCase):
    def test_replace_not_bad(self):
        self.assertEqual('This music is good!', replace_not_bad('This music is not so bad!'))

    def test_v_ing(self):
        self.assertEqual('reading', v('read'))

    def test_v_ly(self):
        self.assertEqual('readingly', v('reading'))

    def test_v_short(self):
        self.assertEqual('eat', v('eat'))
