
# create a dictionary storing student data
student = {
    "name": "Chandu",
    "age": 25,
    "course": "AI Engineering"
}

# print the entire dictionary
print(student)

# print specific values using keys
print("Name:", student["name"])
print("Course:", student["course"])

# add a new key-value pair
student["marks"] = 91

# print updated dictionary
print("Updated:", student)

# loop through dictionary
for key, value in student.items():
    print(key, ":", value)