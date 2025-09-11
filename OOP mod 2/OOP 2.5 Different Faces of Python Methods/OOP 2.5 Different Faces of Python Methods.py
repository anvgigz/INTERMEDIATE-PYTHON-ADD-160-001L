"""
Write a program demonstrating the use of instance, class, and static methods in different scenarios.
"""

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        current_year = 0 #by excluding the self the current_year will apply to all instances of this class

    def display_car_type(self):
        return f"This car is a {self.make} {self.model}"

    @classmethod
    def set_current_year(cls, current_year):
        cls.current_year = current_year
        print(f"Current year set to {cls.current_year}.")
        return

    @staticmethod
    def car_maintenance_tips():
        return "Regularly check tire pressure, oil levels, and brake functionality."
    


Car.set_current_year(2025) #Class Method Call the new instance of new_car will now have the current_year attribute
print(Car.current_year)

new_car = Car("Toyota", "Camry") #Instance Method Call
print(new_car.display_car_type())
print(F"new_car year set to {new_car.current_year}")

print(Car.car_maintenance_tips()) #Static Method Call
#no slef or cls parameter is needed because it does not interact with the class or instance



"""
Instance methoda will require atleast 1 self
used to access or modify and instance attribute

Class Methodsrequire the @classmethod decorator above the class function,
also by using cls.(instance_method) you are able to change the instance attribute 
for all instances of the class.
You cannot use self in a class method because it is not tied to a specific instance.

Static methods require the @staticmethod decotator above the static function.
No self or cls parameter is needed because it does not interact with the class or instance
"""

