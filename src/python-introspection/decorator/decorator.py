def counter(fn):
    count = 0
    
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Function {fn.__name__} was called {count} times")
        return fn(*args, **kwargs)
    return inner


def add(a:int,b:int=0)->int:
    """
    Add to values
    """
    return a+b