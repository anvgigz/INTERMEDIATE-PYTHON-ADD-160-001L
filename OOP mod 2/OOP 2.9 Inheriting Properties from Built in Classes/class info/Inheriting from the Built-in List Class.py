
class CustomList(list):
    def __init__(self, *args):
        super().__init__(*args)

    def append(self, item):
        if isinstance(item, tuple) and len(item) == 3 and self._is_valid(*item):
            super().append(item)
        else:
            print("Invalid item. Only tuples with three integers between 1 and 40 are allowed.")

    def _is_valid(self, a, b, c):
        return all(isinstance(i, int) and 1 <= i <= 40 for i in (a, b, c))

# Create an instance of CustomList
my_list = CustomList()

# Try to append valid and invalid items
my_list.append((10, 20, 30))  # Valid tuple
my_list.append((5, 50, 15))   # Invalid tuple
print(my_list)  # Output: [(10, 20, 30)]