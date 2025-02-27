fruit_prices = {
    "apple" : 0.50,
    "banana" : 0.75,
    "orange" : 0.80
}

# Update the fruit(key) orange with grape and item price

for i in fruit_prices.copy():

    if i == "orange":

        fruit_prices.pop(i)

        fruit_prices["Grape"] = 1

print(fruit_prices)

