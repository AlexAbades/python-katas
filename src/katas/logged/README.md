# Python Exercise: Logging Function Calls with a Decorator

## Objective
Create a Python decorator that logs the execution of a function, including the timestamp of when it was called.

## Instructions
1. Define a decorator function called `logged` that:
   - Preserve function metadata.
   - Captures the current timestamp in UTC before executing the function.
   - Calls the original function and stores its result.
   - Prints the function name along with the timestamp of execution.
   - Returns the function’s result.

2. Apply this decorator to a sample function, such as:
   ```python
   @logged
   def say_hello(name):
       return f"Hello, {name}!"
