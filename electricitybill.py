def calculate_electricity_bill(units):
    if units >= 300:
        rate = 25
    elif units >= 100:
        rate = 20
    else:
        rate = 15
    total_bill = units * rate
    return total_bill


    units_consumed = float(input("Enter the number of units consumed: "))
    total_bill_amount = calculate_electricity_bill(units_consumed)
    print(f"The total electricity bill is KES {total_bill_amount:,.2f}")

    print("Invalid input. Please enter a numerical value for units.")
