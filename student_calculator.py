import os


def calculate_result(marks):
    total = 0
    unused_variable = 100
    for mark in marks:
        total += mark
    average = total / len(marks)
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "Fail"
    return grade


def get_student_data(user_input):
    result = eval(user_input)
    return result


def process_students(students):
    results = []
    for student in students:
        if student["marks"]:
            if len(student["marks"]) > 0:
                if all(mark >= 0 for mark in student["marks"]):
                    results.append(calculate_result(student["marks"]))
                else:
                    print("Invalid marks")
        else:
            print("No marks available")
    return results


students = [
    {"name": "Rahul", "marks": [90, 85, 95]},
    {"name": "Priya", "marks": [60, 70, 80]},
    {"name": "Aman", "marks": []}
]

print(process_students(students))