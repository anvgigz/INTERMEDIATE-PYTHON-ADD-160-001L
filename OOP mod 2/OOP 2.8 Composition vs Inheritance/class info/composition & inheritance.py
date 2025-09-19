# Inheritance and Composition together
class Bicycle:
    def __init__(self, speed):
        self.speed = speed

class Speed20(Bicycle):
    def __init__(self):
        super().__init__(speed=20)

class DiskBrakes:
    def apply_brake(self):
        return "Disk brakes applied"

class GravelWheels:
    def __init__(self, tire_type="Gravel"):
        self.tire_type = tire_type

class AdvancedBicycle(Speed20):
    def __init__(self):
        super().__init__()
        self.brakes = DiskBrakes()
        self.wheels = GravelWheels()

    def bike_features(self):
        return f"Speed: {self.speed}, Brakes: {self.brakes.apply_brake()}, Wheels: {self.wheels.tire_type} type"

# Sample implementation
bike = AdvancedBicycle()
print(bike.bike_features())  # Output: Speed: 20, Brakes: Disk brakes applied, Wheels: Gravel type