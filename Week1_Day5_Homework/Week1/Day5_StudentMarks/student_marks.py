# Week 1 - Day 5
# Student Marks Program

students = {
    "Aarav": [85, 90, 88],
    "Diya": [72, 75, 70],
    "Ishaan": [95, 92, 96],
    "Meera": [64, 68, 66],
    "Rohan": [52, 58, 55]
}

def calculate_average(marks):
    return sum(marks) / len(marks)

def get_grade(average):
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

for student, marks in students.items():
    average = calculate_average(marks)
    grade = get_grade(average)

    print("Student:", student)
    print("Marks:", marks)
    print("Average:", round(average, 2))
    print("Grade:", grade)
    print()
