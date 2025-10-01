import pickle


# Load the pickle files
with open('boys_names.pkl', 'rb') as f:
    boys_names = pickle.load(f)

with open('girls_names.pkl', 'rb') as f:
    girls_names = pickle.load(f)

# Function to check if a name is in the list
def check_name_in_list(name, names_list):
    return name in names_list

# Get a first name from the user
user_name = input("Enter a first name: ").strip()

# Check if the name is in either list
is_in_boys_names = check_name_in_list(user_name, boys_names)
is_in_girls_names = check_name_in_list(user_name, girls_names)

# Output the result
if is_in_boys_names and is_in_girls_names:
    print(f"The name {user_name} is in both boys' and girls' lists.")
elif is_in_boys_names:
    print(f"The name {user_name} is in the boys' list.")
elif is_in_girls_names:
    print(f"The name {user_name} is in the girls' list.")
else:
    print(f"The name {user_name} is not in either list.")

# Annotating the code:
# 1. Import the pickle module for reading the pickle files.
# 2. Load the pickle files into lists using pickle.load().
# 3. Define a function to check if a name is in the list.
# 4. Get a first name from the user using input().
# 5. Strip any extra spaces from the user input.
# 6. Check if the name is in the boys' or girls' list using the defined function.
# 7. Print the appropriate message based on whether the name is found in the boys', girls', both, or neither list.