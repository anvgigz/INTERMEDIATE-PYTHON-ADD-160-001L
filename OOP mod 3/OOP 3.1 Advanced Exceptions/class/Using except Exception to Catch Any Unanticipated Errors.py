
# To catch any unanticipated errors, 
# you can use a general except Exception block.


try:
    # Code that may raise any exception
    result = 10 / 0
except Exception as e:
    print(f"An error occurred: {e}")