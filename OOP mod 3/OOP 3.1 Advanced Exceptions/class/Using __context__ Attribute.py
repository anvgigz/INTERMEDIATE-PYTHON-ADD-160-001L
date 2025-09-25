try:
    try:
        1 / 0
    except ZeroDivisionError as e:
        raise ValueError("A value error occurred")
except ValueError as e:
    print(f"ValueError: {e}")
    print(f"Context: {e.__context__}")
    
# The __context__ attribute is automatically set when an exception is raised while another exception is handled.