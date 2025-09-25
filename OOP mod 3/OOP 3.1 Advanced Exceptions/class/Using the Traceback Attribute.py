import traceback

try:
    1 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
    print("Traceback:")
    traceback.print_tb(e.__traceback__)
    
print("cheese still prints")