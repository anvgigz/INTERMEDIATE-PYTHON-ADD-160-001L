
# You can explicitly chain exceptions using the from keyword 
# to provide more context to the error.

try:
    try:
        open("non_existent_file.txt")
    except FileNotFoundError as e:
        raise RuntimeError("Failed to open the file") from e
except RuntimeError as e:
    print(f"Caught chained exception: {e}")
    print(f"Original cause: {e.__cause__}")

print("cheese still prints")