# OOP 5.1 Metaprogramming Assignment
# Objective: Use the 'type' function to dynamically create a class with at least two methods

# Step 1: Define the class name
class_name = 'SmartPhone'

# Step 2: Choose the base classes (inheriting from object)
base_classes = (object,)

# Step 3: Create the methods
# Define methods as functions that will become class methods
def make_call(self, number):
    """Method to simulate making a phone call"""
    return f"Calling {number}..."

def send_text(self, recipient, message):
    """Method to simulate sending a text message"""
    return f"Sending text to {recipient}: '{message}'"

def take_photo(self):
    """Method to simulate taking a photo"""
    return "📸 Photo taken!"

def play_music(self, song):
    """Method to simulate playing music"""
    return f"🎵 Now playing: {song}"

# Step 4: Create the dictionary of methods and attributes
class_dict = {
    'make_call': make_call,
    'send_text': send_text,
    'take_photo': take_photo,
    'play_music': play_music,
    'brand': 'TechCorp',  # Class attribute
    'model': 'SmartX Pro'  # Class attribute
}

# Step 5: Create the class using 'type'
# Syntax: type(name, bases, dict)
SmartPhone = type(class_name, base_classes, class_dict)

# Step 6: Instantiate the class and test the methods
print("=== Testing Dynamically Created SmartPhone Class ===")
print()

# Create an instance of the dynamically created class
my_phone = SmartPhone()

# Test all methods
print("Testing make_call method:")
print(my_phone.make_call("555-1234"))
print()

print("Testing send_text method:")
print(my_phone.send_text("Alice", "Hello, how are you?"))
print()

print("Testing take_photo method:")
print(my_phone.take_photo())
print()

print("Testing play_music method:")
print(my_phone.play_music("Shape of You - Ed Sheeran"))
print()

# Test class attributes
print("Testing class attributes:")
print(f"Brand: {my_phone.brand}")
print(f"Model: {my_phone.model}")
print()

# Demonstrate special attributes
print("=== Exploring Special Attributes ===")
print(f"Class name (__name__): {SmartPhone.__name__}")
print(f"Instance class (__class__): {my_phone.__class__}")
print(f"Base classes (__bases__): {SmartPhone.__bases__}")
print(f"Class dictionary keys: {list(SmartPhone.__dict__.keys())}")
print()

# Verify the type of our dynamically created class
print("=== Metaclass Information ===")
print(f"Type of SmartPhone class: {type(SmartPhone)}")
print(f"Is SmartPhone an instance of type? {isinstance(SmartPhone, type)}")

print("\n Assignment completed successfully!")
print("This demonstrates dynamic class creation using the 'type' function with:")
print("- Custom class name")
print("- Base class inheritance")
print("- Multiple methods with different functionalities")
print("- Class attributes")
print("- Proper testing and documentation")