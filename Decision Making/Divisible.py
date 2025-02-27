
# Enter a number by user

# Check wheather the number is divisible both 2 and 3, print "Divisible by both"

# Check number divisible only by 2 and not 3 >> Divisible only by 2

# Check number divisible by either 2 or 3 >> (Either 2 or 3)

# Check number not dividible by both 2 and 3 >> (Not divisible by 2 and 3)

num = int(input("Enter the number:"))

if num % 2 == 0 and num % 3 == 0:
    
    print(f"{num} Divisible by both")

elif num % 2 == 0 and num % 3 != 0:

    print(f"{num} Divisible only by 2")

elif num % 2 == 0 or num % 3 == 0:

    print(f"{num} Divisible by either 2 or 3")

elif num % 2 != 0 and num % 3 != 0:

    print(f"{num} Not divisible by 2 and 3")

