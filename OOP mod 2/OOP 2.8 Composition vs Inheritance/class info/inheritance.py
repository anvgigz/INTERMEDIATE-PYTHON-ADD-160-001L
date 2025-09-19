
# Example of inheritance
class Dog:
    """A class representing a dog.
    """
    def __init__(self, name):
        self.name = name
        
    def bark(self):
        return "Woof!"

class GermanShepherd(Dog):
    def guard(self):
        return "I am guarding the house!"

# Sample implementation
dog = GermanShepherd("Rex")
print(dog.bark())  # Output: Woof!
print(dog.guard())  # Output: I am guarding the house!