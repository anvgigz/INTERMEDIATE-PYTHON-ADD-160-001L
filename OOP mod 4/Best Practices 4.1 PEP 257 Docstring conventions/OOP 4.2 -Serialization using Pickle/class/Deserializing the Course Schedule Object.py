import pickle

# Deserialize the course schedule object from the file
with open('course_schedule.pkl', 'rb') as f:
    loaded_course_schedule = pickle.load(f)

print(loaded_course_schedule)

# Annotating the code:
# 1. Open the file named 'course_schedule.pkl' in read-binary mode ('rb').
# 2. Deserialize the course schedule object from the file using pickle.load().
# 3. Print the deserialized course schedule object.