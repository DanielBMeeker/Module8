import unittest
import datetime
from more_fun_with_collections import half_birthday as hb


class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        birthday = datetime.datetime(2020, 10, 7)
        self.assertEqual((2021, 4, 7), hb.half_birthday(birthday))


if __name__ == '__main__':
    unittest.main()
