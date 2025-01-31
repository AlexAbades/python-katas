from functools import reduce


def fibonacci_recursive(n: int) -> int:
    return 1 if n < 3 else fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_loop(n: int) -> int:
    fib_1 = 1
    fib_2 = 1
    for i in range(3, n + 1):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_2

def fibonacci_functional(n:int)->int:
    initial = (0,1)
    dummy = range(n)
    fib_n = reduce(lambda prev,n: (prev[0]+prev[1], prev[0]),dummy, initial)
    return fib_n[0]


if __name__ == "__main__":
    print(fibonacci_recursive(100))
