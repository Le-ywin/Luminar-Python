# Cost of bike above 100000, add 15% tax to the price

# If the bike price is between 50k and 100k, add 10% tax to the price

# if the bike price is below 50k, 7% tax is added to the price

price = int(input("Enter the price of the Bike:"))

if price > 100000:

    tax = price * 0.15

    print(f"Your total price is {price + tax}")

elif price > 50000 and price <= 100000:

    tax = price * 0.10

    print(f"Your total price is {price + tax}")

else:

    tax = price * 0.07

    print(f"Your total price is {price + tax}")

