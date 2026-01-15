def determine_student_grade(mark):
    if mark >= 70:
        grade = "A"
    elif mark >= 60:
        grade = "B"
    elif mark >= 50:
        grade = "C"
    elif mark >= 40:
        grade = "D"
    else:
        grade = "Fail"
    return grade


    student_mark = float(input("Enter student mark: "))
    student_grade = determine_student_grade(student_mark)
    print(f"The student's grade is: {student_grade}")

    print("Invalid input. Please enter a numerical value for the mark.")
