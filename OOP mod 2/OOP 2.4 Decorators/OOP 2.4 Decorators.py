import time
from functools import wraps

"""
Programming Assignments
Create a new decorator:
Write a decorator that logs the execution time of a function. Apply this decorator to a few sample functions and measure their execution times. (Estimated time: 30 minutes)

Modify the drive decorator:
Enhance the drive_decorator to log the time taken for each drive action. Use the time module to capture the start and end times. (Estimated time: 45 minutes)

Implement a caching decorator:
Create a decorator that caches the results of a function to avoid repeated calculations. Test it with a computationally intensive function. (Estimated time: 1 hour)

Create a parameterized decorator:
Write a decorator that takes an argument specifying the number of times the decorated function should be executed. Apply it to a function and test with different argument values. (Estimated time: 1 hour 30 minutes)

Upload your finished assignments to your GitHub directory for the course and submit the link.
"""



# 1. Decorator to log execution time
def time_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end - start:.6f} seconds")
        return result
    return wrapper

# Sample functions to test time_logger
@time_logger
def slow_add(a, b):
    time.sleep(0.5)
    return a + b

@time_logger
def slow_multiply(a, b):
    time.sleep(0.3)
    return a * b

# 2. Modify drive_decorator to log time
def drive_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Starting drive action...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Drive action took {end - start:.6f} seconds")
        return result
    return wrapper

# Example usage of drive_decorator
@drive_decorator
def drive(distance):
    time.sleep(0.2)
    print(f"Driving {distance} miles.")

# 3. Caching decorator
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

# Example computationally intensive function
@cache_decorator
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 4. Parameterized decorator to repeat function
def repeat(num_times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(num_times):
                print(f"Execution {i+1} of {num_times}")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# Example usage of repeat decorator
@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

# --- Sample calls to test the decorators ---
if __name__ == "__main__":
    print(slow_add(2, 3))
    print(slow_multiply(4, 5))
    drive(10)
    print(f"Fibonacci(10): {fibonacci(10)}")
    greet("Sam")


