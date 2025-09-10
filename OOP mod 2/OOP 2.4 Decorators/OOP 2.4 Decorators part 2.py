import time
from functools import wraps

"""
Assignment: Class-based Decorators
Objective:
Develop and use class-based decorators, including those with arguments and the __call__ method.

Instructions:
- Create a class-based decorator TimingDecorator that measures and prints the execution time of a function.
- Apply it to a computationally intensive function.
- Test the decorated function with a large input value.
- Experiment with other functions to observe timing behavior.
"""

# Step 1: Define the class-based TimingDecorator
class TimingDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        duration = end - start
        # Only print if execution time is significant
        if duration > 0.0001:
            print(f"{self.func.__name__} executed in {duration:.6f} seconds")
        return result

# Step 2: Optional cache decorator to improve performance
def cache_decorator(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"Fetching cached result for {args}")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper
# Step 3: Computationally intensive function - Fibonacci
@cache_decorator
@TimingDecorator
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Step 4: Test the decorated function
print("Calculating Fibonacci(100):")
fibonacci_result = fibonacci(100)
print(f"Fibonacci(100): {fibonacci_result}")

# Step 5: Experiment with another function - Factorial
@TimingDecorator
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("\nCalculating Factorial(20):")
factorial_result = factorial(20)
print(f"Factorial(20): {factorial_result}")
