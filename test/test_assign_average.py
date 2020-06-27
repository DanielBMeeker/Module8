import unittest
from more_fun_with_collections import assign_average as aa

a_dict = {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}


class MyTestCase(unittest.TestCase):
    def test_switch_average_A(self):
        self.assertEqual(90, aa.switch_average(a_dict, 'A'))
        self.assertEqual(90, aa.switch_average(a_dict, 'a'))

    def test_switch_average_B(self):
        self.assertEqual(80, aa.switch_average(a_dict, 'B'))
        self.assertEqual(80, aa.switch_average(a_dict, 'b'))

    def test_switch_average_C(self):
        self.assertEqual(70, aa.switch_average(a_dict, 'C'))
        self.assertEqual(70, aa.switch_average(a_dict, 'c'))

    def test_switch_average_D(self):
        self.assertEqual(60, aa.switch_average(a_dict, 'D'))
        self.assertEqual(60, aa.switch_average(a_dict, 'd'))

    def test_switch_average_F(self):
        self.assertEqual(0, aa.switch_average(a_dict, 'F'))
        self.assertEqual(0, aa.switch_average(a_dict, 'f'))

    def test_switch_average_non_key(self):
        with self.assertRaises(ValueError):
            aa.switch_average(a_dict, 'S')


if __name__ == '__main__':
    unittest.main()
