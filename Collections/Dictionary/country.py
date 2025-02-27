"""

Create a dictionary of five countries and their capitals. User need to input a country name if the country name in the dictionary return its capital
and if it is not in the dictionary return "Not found"

"""

new = {"afghanistan" : "Kabul","albania" : "tirana","Algeria" : "algiers","Andorra" : "vella","Angola" : "luanda","india" : "delhi"}

name = input("Enter the Country name: ")

name = name.lower()

if name in new:

    print(new[name])

else:

    print("Not found!")

