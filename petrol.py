def calculate_fuel_cost(litres):
    if litres >= 50:
        price_per_litre = 170
    elif litres >= 20:
        price_per_litre = 175
    else:
        price_per_litre = 180
    total_cost = litres * price_per_litre
    return total_cost


    litres_purchased = float(input("Enter the number of litres purchased: "))
    total_cost_of_fuel = calculate_fuel_cost(litres_purchased)
    print(f"The total cost of fuel is KES {total_cost_of_fuel:,.2f}")
    print("Invalid input. Please enter a numerical value for litres.")
