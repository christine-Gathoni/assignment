def calculate_density(mass, volume):
    if volume == 0:
        return "Error: Volume cannot be zero"
    density = mass / volume
    return density

    object_mass = float(input("Enter mass (in kg): "))
    object_volume = float(input("Enter volume (in m³): "))
    object_density = calculate_density(object_mass, object_volume)
    if isinstance(object_density, str):
        print(object_density)
    else:
        print(f"The density of the object is {object_density:.2f} kg/m³")

    print("Invalid input. Please enter numerical values for mass and volume.")
