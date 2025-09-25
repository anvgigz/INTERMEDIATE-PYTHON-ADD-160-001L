try:
    # Code that may raise an exception
    number = int(input("Enter a number: "))
except ValueError:
    # Code to handle the exception
    print("That's not a valid number!")