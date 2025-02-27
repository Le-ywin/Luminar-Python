# Check the Smallest among three numbers



a = int(input("Enter the 1st No: "))

b = int(input("Enter the 2nd No: "))

c = int(input("Enter the 3rd No: "))

if a < b and a < c:

    smallest = a

elif b < a and b < c:

    smallest = b

else:

    smallest = c

print(f"The smallest number is {smallest}")  




# Second smallest among three numbers


if a <= b and b <= c:

    smallest = b

elif a <= c and c <= b:

    smallest = c

else:

    smallest = a

print(f"Second smallest number is {smallest}")

