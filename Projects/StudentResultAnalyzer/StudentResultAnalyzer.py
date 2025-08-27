students = []
subjects = ["Math", "Science", "Computer", "Social", "Health"]

while True:
    student = {}
    while True:
        student["student_id"] = input("Enter Student ID: ")
        if student["student_id"] in [Id["student_id"] for Id in students]:
            print("ID already exits. Enter again...")
        else:
            break

    student["name"] = input("Enter Student Name: ")

    while True:
        student["student_class"] = input("Enter Student Class: ")
        if student["student_class"].strip() == "":
            print("Enter again")
        else:
            break

    print("Enter Student Marks")
    marks = {}
    for subject in subjects:
        while True:
            try:
                mark = int(input(f"Enter marks of {subject}"))
                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                else:
                    print("Marks must be between 0 and 100. Try again.")
            except ValueError:
                print("Invalid input. Enter a number.")
    student["marks"] = marks

    # Calculate Total
    total = 0
    for mark in marks.values():
        total += mark
    student["total"] = total

    # Calculate Percentage
    total_subject = len(subjects)
    full_marks = total_subject * 100
    percentage = (student["total"] / full_marks) * 100
    student["percentage"] = percentage

    # Assign Grade
    if percentage >= 90:
        student["grade"] = "A+"
    elif percentage >= 80:
        student["grade"] = "A"
    elif percentage >= 70:
        student["grade"] = "B+"
    elif percentage >= 60:
        student["grade"] = "B"
    elif percentage >= 50:
        student["grade"] = "C+"
    elif percentage >= 40:
        student["grade"] = "C"
    elif percentage >= 30:
        student["grade"] = "D+"
    else:
        student["grade"] = "F"

    students.append(student)

    repeat = input("Do you want to add more student (yes/no): ")
    if repeat.lower() == "no":
        break

# Display All Students:
print("All Students Record")
space = " "
print(f"{'ID':<5} {'Name':<10} {'Class':<6} {'Math':<5} {'Science':<7} {'Computer':<8} {'Social':<6} {'Health':<6} "
      f"{'Total':<5} {'%':<6} {'Grade':<5}")


for s in students:
    print(f"{s['student_id']:<5} {s['name']:<10} {s['student_class']:<6} "
          f"{s['marks']['Math']:<5} {s['marks']['Science']:<7} {s['marks']['Computer']:<8} "
          f"{s['marks']['Social']:<6} {s['marks']['Health']:<6} {s['total']:<5} "
          f"{s['percentage']:<6.2f} {s['grade']:<5}")

students_grade = {}
A_plus, A, B_plus, B, C_plus, C, D_plus, F = 0, 0, 0, 0, 0, 0, 0, 0
for s in students:
    if s["grade"] == "A+":
        A_plus += 1
        students_grade["A+"] = A_plus
    elif s["grade"] == "A":
        A += 1
        students_grade["A"] = A
    elif s["grade"] == "B+":
        B_plus += 1
        students_grade["B+"] = B_plus
    elif s["grade"] == "B":
        B += 1
        students_grade["B"] = B
    elif s["grade"] == "C+":
        C_plus += 1
        students_grade["C+"] = C_plus
    elif s["grade"] == "C":
        C += 1
        students_grade["C"] = C
    elif s["grade"] == "D+":
        D_plus += 1
        students_grade["D+"] = D_plus
    else:
        student["grade"] = "F"
        F += 1


students_grade = {}
for s in students:
    grade = s["grade"]
    students_grade[grade] = students_grade.get(grade, 0) + 1

print(f"Total Pass Students: {A_plus + A + B_plus + B_plus + C_plus + D_plus}")
print(f"Total Fail Students: {F}")

print(f"{'Grade':<10} {'No.of Students':<10}")
for grade, count in students_grade.items():
    print(f"{grade:<10} {count:<10}")

print(students_grade)
