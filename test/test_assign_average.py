import unittest
from more_fun_with_collections import assign_average as aa


class MyTestCase(unittest.TestCase):
    def test_switch_average_A(self):
        self.assertEqual(90, aa.switch_average('A'))
        self.assertEqual(90, aa.switch_average('a'))

    def test_switch_average_B(self):
        self.assertEqual(80, aa.switch_average('B'))
        self.assertEqual(80, aa.switch_average('b'))

    def test_switch_average_C(self):
        self.assertEqual(70, aa.switch_average('C'))
        self.assertEqual(70, aa.switch_average('c'))

    def test_switch_average_D(self):
        self.assertEqual(60, aa.switch_average('D'))
        self.assertEqual(60, aa.switch_average('d'))

    def test_switch_average_F(self):
        self.assertEqual(0, aa.switch_average('F'))
        self.assertEqual(0, aa.switch_average('f'))

    def test_switch_average_non_key(self):
        self.assertRaises(ValueError)
        aa.switch_average('S')


if __name__ == '__main__':
    unittest.main()
