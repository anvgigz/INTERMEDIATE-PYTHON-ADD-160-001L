import copy

# Step 1: Create a nested list
nested_list = [[1, 2, 3], [4, 5, 6]]

# Step 2: Make a shallow copy
shallow_nested_copy = nested_list[:]

# Step 3: Make a deep copy
deep_nested_copy = copy.deepcopy(nested_list)

# Step 4: Modify an element in one of the inner lists of the shallow copy
shallow_nested_copy[0][2] = "modified"

# Step 5: Modify an element in one of the inner lists of the deep copy
deep_nested_copy[1][2] = "modified"

# Step 6: Print all three lists
print("Original nested_list:", nested_list)
print("Shallow copy shallow_nested_copy:", shallow_nested_copy)
print("Deep copy deep_nested_copy:", deep_nested_copy)

# Step 7: Explanation
print("\nExplanation:")
print("- The original nested_list reflects the change made in the shallow copy because they share inner list references.")
print("- The deep copy remains unaffected because it is a completely independent copy.")
