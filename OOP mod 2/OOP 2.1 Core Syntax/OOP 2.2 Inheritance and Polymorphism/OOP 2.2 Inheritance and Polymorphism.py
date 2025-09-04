
class Collar:
    def __init__(self, color, size):
        self.color = color
        self.size = size

class Dog:
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

class Owner:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class PetProfile(Dog, Collar, Owner):
    def __init__(self, breed, dog_color, collar_color, collar_size, owner_name, owner_phone):
        Dog.__init__(self, breed, dog_color)
        Collar.__init__(self, collar_color, collar_size)
        Owner.__init__(self, owner_name, owner_phone)

    def describe(self):
        return (
            f"{self.name} owns a {self.color} {self.breed} dog "
            f"with a {self.color} collar (size {self.size}). "
            f"Contact: {self.phone}"
        )


pet = PetProfile(
    breed="Labrador",
    dog_color="black",
    collar_color="red",
    collar_size="medium",
    owner_name="Stephen",
    owner_phone="555-1234"
)

print(pet.describe())
