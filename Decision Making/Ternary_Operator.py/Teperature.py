# Temp less than 20 >> Cold

# Temp b/t 20 to 30 (inclusive) >>Warm

# Temp > 30 >> Hot

temp = int(input("Enter the Temperature: "))

print("Cold" if temp < 20 else "Warm" if temp >= 20 and temp <= 30 else "Hot")

