import pickle

# Define the course schedule object
course_schedule = {
    'classroom': 'Room 101',
    'building': 'Science Hall',
    'number_of_seats': 30,
    'computers': True
}

# Serialize the course schedule object to a file
with open('course_schedule.pkl', 'wb') as f:
    pickle.dump(course_schedule, f)

# Annotating the code:
# 1. Import the pickle module.
# 2. Define a dictionary representing the course schedule.
# 3. Open a file named 'course_schedule.pkl' in write-binary mode ('wb').
# 4. Serialize the course schedule object and write it to the file using pickle.dump().