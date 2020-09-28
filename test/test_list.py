from unittest import TestCase
from list1 import me, sort_pairs, fx


class ListTest(TestCase):
    def test_me_empty(self):
        input_list = []
        expected = 0
        self.assertEqual(expected, me(input_list))

    def test_me_no_match_by_length(self):
        input_list = ["1", "", "a", "ab"]
        expected = 0
        self.assertEqual(expected, me(input_list))

    def test_me_no_match_by_symbol_equality(self):
        input_list = ["abc", "cbd", "epp"]
        expected = 0
        self.assertEqual(expected, me(input_list))

    def test_me_match(self):
        input_list = ["abba", "pep"]
        expected = 2
        self.assertEqual(expected, me(input_list))

    def test_fx(self):
        input_list = ['tix', 'xyz', 'apple', 'xacadu', 'aabbbccc']
        expected_list = ['xacadu', 'xyz', 'aabbbccc', 'apple', 'tix']
        self.assertEqual(expected_list, fx(input_list))

    def test_fx_empty_str(self):
        input_list = ['', 'xyz', 'apple', 'xacadu', 'aabbbccc']
        expected_list = ['xacadu', 'xyz', '', 'aabbbccc', 'apple']
        self.assertEqual(expected_list, fx(input_list))

    def test_sort_tuples(self):
        input_list = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
        expected_list = [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
        self.assertEqual(expected_list, sort_pairs(input_list))
