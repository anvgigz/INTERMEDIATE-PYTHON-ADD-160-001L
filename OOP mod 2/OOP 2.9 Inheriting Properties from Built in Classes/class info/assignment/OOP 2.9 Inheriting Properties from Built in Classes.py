class VowelString(str):
    """
    A custom string class that inherits from Python's built-in `str` class.
    Adds functionality to count the number of vowels in the string.

    Args:
        str (str): The base string to extend.
    """

    def __init__(self, value):
        """
        Initialize the custom string.

        Note: Since `str` is immutable, __init__ is not ideal for initialization.
        This constructor does not store `value` because it's already handled by `str`.
        """
        super().__init__()  # No need to pass value here; handled by __new__

    def vowel_count(self):
        """
        Count the number of vowels in the string.

        Returns:
            int: The number of vowels (a, e, i, o, u) in both uppercase and lowercase.
        """
        vowels = "aeiouAEIOU"  # Define vowels to check against
        return sum(1 for char in self if char in vowels)  # Count vowels using generator expression
# Create an instance of VowelString with a sample string
my_string = VowelString("Hello World")

# Print the original string
print("Original string:", my_string)

# Print the number of vowels in the string
print("Number of vowels:", my_string.vowel_count())
