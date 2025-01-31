def timed(fn, count):
    """
    A decorator that measures the average execution time of a function over a specified number of runs.
    Args:
        fn (callable): The function to be timed.
        count (int): The number of times to execute the function for timing.
    Returns:
        callable: A wrapped function that, when called, executes the original function and prints the average execution time.
    Example:
        @timed
        def my_function():
            # function implementation
        my_function()
    """

    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        elapsed_total = 0

        for i in range(count):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter

            elapsed_time = end - start
            elapsed_total += elapsed_time

        elapsed_avg = elapsed_total / count

        return result, elapsed_avg

    return inner
