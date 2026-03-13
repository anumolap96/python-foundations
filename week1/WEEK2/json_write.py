
import json

# create dictionary
student = {
    "name": "Chandu",
    "age": 25,
    "course": "AI Engineering",
    "marks": 91
}

# open file in write mode
with open("student.json", "w") as file:
    
    # convert dictionary to JSON and save
    json.dump(student, file)

print("JSON file created")