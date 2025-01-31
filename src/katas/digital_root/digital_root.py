from functools import reduce
from operator import add


def digital_root_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("Number should be positive")

    if not n // 10:
        return n

    number = reduce(add, map(int, str(n)))
    return digital_root_recursive(number)


def digital_root_while(n: int) -> int:
    if n < 0:
        raise ValueError("Number should be positive")

    while n >= 10:
        n = reduce(add, map(int, str(n)))

    return n


def digital_root_module(n: int) -> int:
    if n < 0:
        raise ValueError("Number should be positive")

    return 9 if n % 9 == 0 else n % 9
