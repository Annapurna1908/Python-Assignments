import json

# Open the JSON file
with open("student.json", "r") as file:
    data = json.load(file)

# Print formatted output
print("===== STUDENT DETAILS =====")
print("Name:", data["name"])
print("Roll Number:", data["roll_number"])
print("Course:", data["course"])
print("Marks:", data["marks"])