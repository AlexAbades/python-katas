# Python Exercise: Function Execution Timer using a Decorator

## Objective
Create a Python decorator that measures the average execution time of a function over multiple runs.

## Instructions
1. Define a decorator function called `timing_decorator` that:
   - Accepts a function as input.
   - Runs the function multiple times (e.g., 10 times).
   - Measures the execution time for each run.
   - Computes and prints the average execution time.
   - Perserves metadata of the passed function.
   - Returns the result and the average time.

2. Apply this decorator to a sample function, such as:
   ```python
   def sample_function():
       total = sum(range(1000000))  # Simulate a time-consuming operation
       return total
