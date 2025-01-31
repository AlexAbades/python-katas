from typing import List


def powers_of_two(n: int) -> List[int]:
    return [1 if not n else 2**i for i in range(n + 1)]


def powers_of_two_bitwise(n) -> List[int]:
    return [1 << i for i in range(n + 1)]
