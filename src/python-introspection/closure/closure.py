def counter(fn):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Function {fn.__name__} was called {count} times")
        return fn(*args, **kwargs)
    return inner


def add(a, b=0):
    return a + b


add = counter(add)

if __name__ == "__main__":
    result = add(1, 2)
