# test_car_encapsulation.py

from test_car_encapsulation import Car

def test_attribute_access():
    """
    Test direct access to protected attributes.
    """
    car = Car("Toyota", "Camry", 15, 5)
    print("Attempting direct access to _make:")
    try:
        print(car._make)  # Technically accessible, but discouraged
        car._make = "Ford"
        print("Modified _make directly:", car._make)
    except AttributeError as e:
        print("Access denied:", e)

def test_getters_setters():
    """
    Test access and modification using getters and setters.
    """
    car = Car("Honda", "Civic", 12, 3)
    print("Original make:", car.make)
    car.make = "Nissan"
    print("Updated make:", car.make)

    print("Original gas level:", car.gas_level)
    car.gas_level = 20  # Should be capped at tank size
    print("Updated gas level (capped):", car.gas_level)

def test_method_functionality():
    """
    Test Car methods like add_gas and car_info.
    """
    car = Car("Chevrolet", "Corvette", 18, 5)
    car.add_gas(10)
    print("After adding gas:", car.car_info())

# Run all tests
if __name__ == "__main__":
    print("=== Testing Attribute Access ===")
    test_attribute_access()
    print("\n=== Testing Getters and Setters ===")
    test_getters_setters()
    print("\n=== Testing Method Functionality ===")
    test_method_functionality()