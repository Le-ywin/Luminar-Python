# User should enter 2 numbers

# Check both are even 

# Check either a or b is even

a = int(input("Enter the 1st No: "))

b = int(input("Enter the 2nd No: "))

if a % 2 == 0 and b % 2 == 0:

    print("Both are Even.")

elif a % 2 == 0 or b % 2 == 0:

    print("Either a or b is Even.")

else:

    print("Both are Odd")