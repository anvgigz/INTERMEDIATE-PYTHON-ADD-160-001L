from test_car_encapsulation import Car  # Assuming Car class is in car.py

def test_attribute_access():
    """
    Test direct access to protected attributes.
    """
    car = Car("Toyota", "Camry", 15, 5)

    # Simulate enforcement of encapsulation
    if hasattr(car, "_make"):
        raise AssertionError("Cannot access private attribute '_make' directly")

    if hasattr(car, "_model"):
        raise AssertionError("Cannot access private attribute '_model' directly")

def test_getters_setters():
    """
    Test access and modification using getters and setters.
    """
    car = Car("Honda", "Civic", 12, 3)
    assert car.make == "Honda"
    car.make = "Nissan"
    assert car.make == "Nissan"

    assert car.gas_level == 3
    car.gas_level = 20  # Should be capped at tank size
    assert car.gas_level == 12

def test_method_functionality():
    """
    Test Car methods like add_gas and car_info.
    """
    car = Car("Chevrolet", "Corvette", 18, 5)
    car.add_gas(10)
    assert car.gas_level == 15
    expected_info = "Make: Chevrolet, Model: Corvette, Tank Size: 18 gallons, Gas Level: 15 gallons"
    assert car.car_info() == expected_info

# Run all tests
if __name__ == "__main__":
    try:
        test_attribute_access()
    except AssertionError as e:
        print(f"AssertionError: {e}")

    try:
        test_getters_setters()
        test_method_functionality()
        print("All tests passed!")
    except AssertionError as e:
        print(f"AssertionError: {e}")
