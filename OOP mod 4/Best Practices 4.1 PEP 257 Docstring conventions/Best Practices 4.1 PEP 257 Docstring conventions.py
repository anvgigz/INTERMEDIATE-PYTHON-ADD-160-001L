"""
Calculator_module.py

A simple calculator class that supports basic arithmetic operations.
Includes methods for Addition, Subtraction, Multiplication, Division,
Clear, and Get Value. and retrieves the current value.
Exception handling implement."""


class Calculator:
    """
    A basic calculator class to perform arithmetic operations.

    Attributes:
        value (float): The current value stored in the calculator.
    """

    def __init__(self, value=0):
        """
        Initializes the calculator with an optional starting value.

        Parameters:
            value (float): Initial value for the calculator. Defaults to 0.
        """
        self.value = value

    def add(self, num):
        """
        Adds a number to the current value.

        Parameters:
            num (float): The number to add.
        """
        self.value += num

    def subtract(self, num):
        """
        Subtracts a number from the current value.

        Parameters:
            num (float): The number to subtract.
        """
        self.value -= num

    def multiply(self, num):
        """
        Multiplies the current value by a number.

        Parameters:
            num (float): The number to multiply by.
        """
        self.value *= num

    def divide(self, num):
        """
        Divides the current value by a number.

        Parameters:
            num (float): The number to divide by.

        Raises:
            ValueError: If attempting to divide by zero.
        """
        if num != 0:
            self.value /= num
        else:
            raise ValueError("Cannot divide by zero")

    def clear(self):
        """
        Resets the calculator's value to zero.
        """
        self.value = 0

    def get_value(self):
        """
        Returns the current value of the calculator.

        Returns:
            float: The current value.
        """
        return self.value

def main():
    """
    Demonstrates usage of the Calculator class with sample operations.
    Includes exception handling for division by zero.
    """
    calc = Calculator()
    calc.add(10)
    calc.subtract(2)
    calc.multiply(5)

    try:
        calc.divide(0)  # This will raise an exception
    except ValueError as e:
        print(e)

    calc.divide(4)
    print(f"Final value: {calc.get_value()}")

    # TODO: Add support for exponentiation and modulus operations
    # TODO: Implement a command-line interface for user input
    # TODO: Make print docstring callable from this module and not automatic

if __name__ == "__main__":
    main()

 # Access and print docstrings to verify
    print("\nModule docstring:")
    print(__doc__)

    print("\nClass docstring:")
    print(Calculator.__doc__)

    print("\nMethod docstring (divide):")
    print(Calculator.divide.__doc__)

    print("\nUsing help() on Calculator:")
    help(Calculator)

