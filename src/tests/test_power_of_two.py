import unittest

from katas.powers_of_two.powers_of_two import powers_of_two, powers_of_two_bitwise


class TestPowerOfTwo(unittest.TestCase):

    def test_correct_function_test(self):
        self.assertTrue(True)

    def test_power_of_two_case_0(self):
        self.assertEqual(powers_of_two(0), [1])

    def test_power_of_two_case_1(self):
        self.assertEqual(powers_of_two(1), [1, 2])

    def test_power_of_two_case_2(self):
        self.assertEqual(powers_of_two(2), [1, 2, 4])

    def test_power_of_two_bitwise(self):
        self.assertEqual(powers_of_two_bitwise(0), [1])
        self.assertEqual(powers_of_two_bitwise(1), [1, 2])
        self.assertEqual(powers_of_two_bitwise(2), [1, 2, 4])    
    