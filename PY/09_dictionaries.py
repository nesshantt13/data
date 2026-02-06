# # Dictionaries

student = {
    "name": "Alice",
    "age": 20,
    "grade" : "A",
    "courses" : ["Math", "Science", "English"]
}

del student["grade"]
print(student)


students = [
    {
        "name": "Bob",
        "age": 22,
        "grade": "B",
        "courses": ["History", "Art"]
    },
    {
        "name": "Charlie",
        "age": 23,
        "grade": "C",
        "courses": ["Biology", "Chemistry"]
    }
]

print(students[1])

# # Accessing and modifying
print(student["name"])                 # "Alice"
print(student.get("name"))             # "Alice"
student["age"] = 21                    #Modify value
student["email"] = "alice@email.com"   # Add new key-value

print(student)

# # Dictionary methods
keys = student.keys()
values = student.values()
items = student.items()

print(keys)
print(values)
print(items)

# Iterating through dictionaries
for key in student:
    print(f"{key}: {student[key]}")

for key, value in student.items():
    print(f"{key}: {value}")

    # Nested dictionaries
    company = {
        "employees": {
            "john": {"age": 30, "department": "IT"},
            "jane": {"age": 25, "department": "HR"}
        } }
    














    # # Exercises :

    #1. Create a dictionary called student_rec


# Step 1: Create the student_records dictionary
student_records = {
    "student_001": {
        "name": "John",
        "age": 19,
        "major": "Computer Science",
        "grades": [85, 92, 78]
    },
    "student_002": {
        "name": "Sarah",
        "age": 20,
        "major": "Biology",
        "grades": [90, 88, 95]
    }
}

# Step 2: Perform operations
# Print Sarah's name
print("Sarah's name:", student_records["student_002"]["name"])

# Add new student
student_records["student_003"] = {
    "name": "Mike",
    "age": 18,
    "major": "Math",
    "grades": [82, 79, 91]
}

# Update John's age
student_records["student_001"]["age"] = 20

# Print all student IDs
print("Student IDs:", list(student_records.keys()))

# Calculate Sarah's average grade
sarah_grades = student_records["student_002"]["grades"]
sarah_average = sum(sarah_grades) / len(sarah_grades)
print(f"Sarah's average grade: {sarah_average:.1f}")

# Step 3: Loop through and print student information
print("\nAll Students:")
for student_id, info in student_records.items():
    # print(f"Student ID: {student_id}, Name: {info['name']}, Major: {info['major']}")
    print(f"Student ID: {student_id}, info: {info}")










