import timeit
from unittest import TestCase

from katas.caching_machine.memoization import FibonacciMemoizaton, fibonacci_memo


class TestMemoization(TestCase):

    def test_test(self):
        self.assertTrue(True)

    def test_fib_class_memoization(self):
        f = FibonacciMemoizaton()
        self.assertEqual(f.fibonacci(10), 55)
        self.assertEqual(f.fibonacci(35), 9227465)
        execution_time = timeit.timeit(lambda: f.fibonacci(35), number=1)
        self.assertLess(execution_time, 1, "Function took too long")
        self.assertEqual(f.fibonacci(100), 354224848179261915075)
        execution_time = timeit.timeit(lambda: f.fibonacci(100), number=1)
        self.assertLess(execution_time, 1, "Function took too long")

    def test_fib_decorator_memoization(self):
        self.assertEqual(fibonacci_memo(10), 55)
        self.assertEqual(fibonacci_memo(35), 9227465)
        self.assertEqual(fibonacci_memo(100), 354224848179261915075)

        execution_time = timeit.timeit(lambda: fibonacci_memo(100), number=1)
        self.assertLess(execution_time, 1, "Function took too long")
