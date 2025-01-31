from functools import reduce
from operator import mul


# Recursive no build in functions
def persistent(n: int, counter: int = 0) -> int:

    if not n // 10:
        return counter

    multiplied_number = 1
    for number in str(n):
        multiplied_number *= int(number)

    return persistent(multiplied_number, counter=(counter + 1))


# Recursive, not for loop
def persistent_bugg(n: int, counter: int = 0) -> int:

    if n // 10:
        new_number = reduce(lambda x, y: int(x) * int(y), str(n))
        return persistent_bugg(new_number, counter=(counter + 1))

    return counter


# Non recursive
def persistent_bugger_no_recursion(n: int) -> int:

    counter = 0
    while  n >= 10:
        n = reduce(mul, map(int, str(n)))
        counter += 1
    return counter

