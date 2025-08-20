#toycar class example
class ToyCar:
    toy_type  = "Car" #Class variable

    def __init__(self, brand, color, car_type, motorized):
        self.brand = brand #Instance variable
        self.color = color #Instance variable
        self.car_type = car_type #Instance variable
        self.motorized = motorized #Instance variable

    def play(self):
        print("the toy car moves forward")

    def sound(self):
        print("Vroom")


race_car = ToyCar("Hot Wheels", "red", "race car", motorized=True)
pickup_truck = ToyCar("Tonka", "yellow", "pickup truck", motorized=False)
police_car = ToyCar("Matchbox", "blue", "police car", motorized=True)


# printing class 
print(race_car.__class__)
print(pickup_truck.__class__)
print(police_car.__class__)

print(race_car.__dict__)

race_car.play()
race_car.sound()
