from functools import wraps


class FibonacciMemoizaton:

    def __init__(self):
        self.cache = {1: 1, 2: 1}

    def fibonacci(self, n: int) -> int:
        if n not in self.cache:
            self.cache[n] = self.fibonacci(n - 1) + self.fibonacci(n - 2)
        return self.cache[n]


def memoization(fn):
    cache = dict()

    @wraps(fn)
    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]

    return inner


@memoization
def fibonacci_memo(n: int) -> int:
    return 1 if n < 3 else fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
