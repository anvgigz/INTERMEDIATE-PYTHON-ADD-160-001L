
# Example of composition
class Drinks:
    def __init__(self, quantity):
        self.quantity = quantity
        self.service_fee = 1.0

    def calculate_cost(self):
        return self.quantity * self.service_fee

class Food:
    def __init__(self, total_cost, split_plate=False):
        self.total_cost = total_cost
        self.split_plate = split_plate
        self.split_plate_fee = 3.0

    def calculate_cost(self):
        if self.split_plate:
            return self.total_cost + self.split_plate_fee
        return self.total_cost

class Tip:
    def __init__(self, total_cost):
        self.total_cost = total_cost

    def calculate_tip(self, percentage):
        return self.total_cost * (percentage / 100)

class Bill:
    def __init__(self, drinks, food, tip_percentage):
        self.drinks = drinks
        self.food = food
        self.tip_percentage = tip_percentage

    def calculate_total(self):
        total_cost = self.drinks.calculate_cost() + self.food.calculate_cost()
        tip = Tip(total_cost).calculate_tip(self.tip_percentage)
        return total_cost + tip

# Sample implementation
drinks = Drinks(quantity=3)
food = Food(total_cost=20, split_plate=True)
bill = Bill(drinks, food, tip_percentage=20)
print(bill.calculate_total())  # Output: 28.8