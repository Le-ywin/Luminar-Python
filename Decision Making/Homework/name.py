
firstname = input("Enter your name: ")

if len(firstname) < 5:

    surname = input("Enter your surname: ")

    name = (firstname + surname).upper()

    print(name.replace(" ", ""))

else:

    print(firstname.lower())