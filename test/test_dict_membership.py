"""
Program: test_dict_membership.py
Author: Daniel Meeker
Date: 6/24/2020

This program defines and tests a function that will determine
if an element is in a dictionary or not. This file tests the
function.
"""

import unittest
from more_fun_with_collections import dict_membership as dm

a_dict = {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}
key_in_dict = 'A'
key_not_in_dict = 'S'


class MyTestCase(unittest.TestCase):
    def test_in_dict_true(self):
        self.assertTrue(dm.in_dict(a_dict, key_in_dict))

    def test_in_dict_false(self):
        self.assertFalse(dm.in_dict(a_dict, key_not_in_dict))


if __name__ == '__main__':
    unittest.main()
