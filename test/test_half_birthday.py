"""
Program: half_birthday.py
Author: Daniel Meeker
Date: 6/28/2020

This program defines a half birthday function that calculates
the half birthday of a given birthday. This file tests it.
"""
import unittest
import datetime
from more_fun_with_collections import half_birthday as hb


class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        birthday = datetime.datetime(2020, 10, 7)
        expected = datetime.date(2021, 4, 7).isoformat()
        self.assertEqual(expected, hb.half_birthday(birthday))


if __name__ == '__main__':
    unittest.main()
