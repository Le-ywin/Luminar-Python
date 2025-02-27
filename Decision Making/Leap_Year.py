# To check wheather a year is leap year or not

# Leap year formula for Century Year >> Year % 400 == 0, and Year % 100 == 0

# Leap Year formula for Non-century year >> Year % 4 == 0 and Year % 100 != 0

year = int(input("Enter the year:"))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:

    print(f"{year} is a Leap Year.")

else:

    print(f"{year} is not a Leap Year")

