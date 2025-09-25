


students = ["Alice", "Bob", "Charlie", "Diana"]

physics_students = students[:]  # Creates a copy of the list
print(id(physics_students))  # Different from id(students)

# Modifying the new reference
physics_students.append("Eve")
print(students)  # ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']

print("if we modify the new variable in both examples, we'll see different behaviors:")
# Modifying the copied list
physics_students.append("Frank")
print(students)  # ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
print(physics_students)  # ['Alice', 'Bob', 'Charlie', 'Diana', 'Frank']


print("""------------------------------------
------------------------------------""")
print("""when you use a shallow copy on a list of dictionaries,
both the original and the copy still point to the same dictionary objects in memory.""")

students = [{"name": "Alice"}, {"name": "Bob"}]
physics_students = students[:]
print(physics_students)
physics_students[0]["name"] = "Charlie"

print(students[0]["name"])  # Output: "Charlie"
