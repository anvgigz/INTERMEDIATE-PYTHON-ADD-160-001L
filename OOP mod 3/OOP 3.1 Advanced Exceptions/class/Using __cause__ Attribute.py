try:
    try:
        1 / 0
    except ZeroDivisionError as e:
        raise ValueError("A value error occurred") from e
except ValueError as e:
    print(f"ValueError: {e}")
    print(f"Cause: {e.__cause__}")
    
    
#The __cause__ attribute is explicitly set when you use the from keyword to chain exceptions.