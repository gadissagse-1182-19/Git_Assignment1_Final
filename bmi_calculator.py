# BMI Calculator Script
def calculate_bmi(weight_kg, height_m):
    """Calculate Body Mass Index (BMI)."""
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)
# Example test values
weight = 70  # in kilograms
height = 1.75 # in meters

result = calculate_bmi(weight, height)
print(f"Weight: {weight} kg | Height: {height} m")
print(f"Your Calculated BMI is: {result}")