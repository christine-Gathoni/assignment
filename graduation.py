def calculate_average_and_graduation_status(mark1, mark2, mark3):
    average = (mark1 + mark2 + mark3) / 3
    if average >= 50:
        status = "Eligible for Graduation"
    else:
        status = "Not Eligible for Graduation"
    return average, status


    m1 = float(input("Enter mark for subject 1: "))
    m2 = float(input("Enter mark for subject 2: "))
    m3 = float(input("Enter mark for subject 3: "))
    avg, grad_status = calculate_average_and_graduation_status(m1, m2, m3)
    print(f"The average mark is {avg:.2f}")
    print(f"Status: {grad_status}")
    print("Invalid input. Please enter numerical values for marks.")
