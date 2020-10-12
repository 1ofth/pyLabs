from unittest import TestCase
from list2 import *


class Test(TestCase):
    def test_merge(self):
        a = [1, 3, 4, 7]
        b = [2, 5, 6]
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], merge(a, b))

    def test_merge_a_only(self):
        a = [1, 3, 4, 7]
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], merge(a, []))

    def test_merge_b_only(self):
        b = [2, 5, 6]
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], merge([], b))
