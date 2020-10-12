from unittest import TestCase
from string2 import *


class Test(TestCase):
    def test_replace_not_bad(self):
        self.assertEqual('This music is good!', replace_not_bad('This music is not so bad!'))
