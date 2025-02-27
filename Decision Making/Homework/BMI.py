"""

Metric units: BMI = weight (kg) / [height (m)]^2

Underweight >> Below 18.5

Healthy Weight >> 18.5 to 24.9

Overweight >> 25.0 to 29.0

Obesity >> 30.0  or greater

Severe Obesty >> 40 or over


"""

weight = float(input("Enter your weight: "))

height = float(input("Enter your Height: "))

bmi = (weight / height**2)

print(bmi)

if bmi < 18.5:

    print("You are Underweight>")

elif bmi >= 18.5 and bmi < 25:

    print("You have a Healthy Weight.")

elif bmi >= 25.0 and bmi <= 29.0:

    print("You have Overweight.")

elif bmi >= 30 and bmi < 40:

    print("You have Obesity.")

elif bmi >= 40:

    print("You have Severe Obesty.")

