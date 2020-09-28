from unittest import TestCase
from string1 import *


class StringTests(TestCase):
    def test_num_of_items(self):
        self.assertEqual('Number of: 9', num_of_items(9))

    def test_num_of_items_many(self):
        self.assertEqual('Number of: many', num_of_items(10))

    def test_start_end_symbols(self):
        self.assertEqual('weme', start_end_symbols('welcome'))

    def test_replace_char(self):
        self.assertEqual('bi**le', replace_char('bibble'))

    def test_replace_char_astr(self):
        self.assertEqual('****', replace_char('****'))

    def test_str_mix_3(self):
        self.assertEqual('pix mad', str_mix('max', 'pid'))

    def test_str_mix_2(self):
        self.assertEqual('dig donner', str_mix('dog', 'dinner'))
