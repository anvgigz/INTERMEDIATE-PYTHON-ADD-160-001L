
# What are they
try:
    try:
        1 / 0
    except ZeroDivisionError as e:
        raise ValueError("A value error occurred") from e
except ValueError as e:
    print(f"ValueError: {e}")
    print(f"Original exception: {e.__cause__}")