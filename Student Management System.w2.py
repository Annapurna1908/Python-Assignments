import csv
import os

FILE_NAME = "students.csv"


# Create CSV file if it doesn't exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Roll Number", "Name", "Marks"])


# Add a student
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, marks])

    print("Student added successfully!")


# Search a student
def search_student():
    roll = input("Enter Roll Number to search: ")

    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for student in reader:
            if student["Roll Number"] == roll:
                print("\nStudent Found!")
                print("Roll Number:", student["Roll Number"])
                print("Name:", student["Name"])
                print("Marks:", student["Marks"])
                found = True
                break

    if not found:
        print("Student not found!")


# Delete a student
def delete_student():
    roll = input("Enter Roll Number to delete: ")

    students = []
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for student in reader:
            if student["Roll Number"] == roll:
                found = True
            else:
                students.append(student)

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            fieldnames = ["Roll Number", "Name", "Marks"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(students)

        print("Student deleted successfully!")
    else:
        print("Student not found!")


# Display all students
def display_students():
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        print("\n===== STUDENT DETAILS =====")

        for student in reader:
            print(
                "Roll Number:", student["Roll Number"],
                "| Name:", student["Name"],
                "| Marks:", student["Marks"]
            )


# Main program
create_file()

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. Display All Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        search_student()

    elif choice == "3":
        delete_student()

    elif choice == "4":
        display_students()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")