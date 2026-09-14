def calculate_average(marks):
    return sum(marks) / len(marks)


def assign_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


print("Student Grade Calculator")

marks = []

for i in range(5):
    mark = float(input("Enter marks for subject " + str(i + 1) + ": "))
    marks.append(mark)

average = calculate_average(marks)
grade = assign_grade(average)

print("\nAverage:", average)
print("Grade:", grade)80