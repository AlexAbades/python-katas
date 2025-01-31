from unittest import TestCase

from katas.fibonacci.fibonacci import (
    fibonacci_functional,
    fibonacci_loop,
    fibonacci_recursive,
)


class TestFibonacci(TestCase):

    def test_test(self):
        self.assertTrue(True)

    def test_fibonacci_recursive(self):
        self.assertEqual(fibonacci_recursive(10), 55)
        self.assertEqual(fibonacci_recursive(35), 9227465)
        self.assertEqual(fibonacci_recursive(38), 39088169)

    def test_fibonacci_loop(self):
        self.assertEqual(fibonacci_loop(10), 55)
        self.assertEqual(fibonacci_loop(35), 9227465)
        self.assertEqual(fibonacci_loop(100), 354224848179261915075)

    def test_fibonacci_functional(self):
        self.assertEqual(fibonacci_functional(10), 55)
        self.assertEqual(fibonacci_functional(35), 9227465)
        self.assertEqual(fibonacci_functional(100), 354224848179261915075)
