# Simple tool to calculate a country's development score
# Based on Education, Health, and Income indices
def calculate_hdi(health, education, income):
    # Calculate the average of the three factors
    hdi_score = (health + education + income) / 3
    return hdi_score

print("--- HDI Calculator ---")
# Taking input from the user
health_idx = float(input("Enter Health Index (0 to 1): "))
edu_idx = float(input("Enter Education Index (0 to 1): "))
inc_idx = float(input("Enter Income Index (0 to 1): "))

# Calculating the result
result = calculate_hdi(health_idx, edu_idx, inc_idx)

print(f"\nThe calculated HDI score is: {result:.2f}")

# Basic logic to categorize the result
if result >= 0.8:
    print("Category: High Human Development")
elif result >= 0.5:
    print("Category: Medium Human Development")
else:
    print("Category: Low Human Development")
