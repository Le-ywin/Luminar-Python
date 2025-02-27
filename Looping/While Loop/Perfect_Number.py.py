# Perfect Numbers

# a positive iteger that is equal to the sum of its proper divisors, which all of its divisors ecluding the number itself


num = int(input("Enter a No: "))

i = 1

sum = 0

while i < num:

    if num % i == 0:

        print(i)

        sum = sum + i

    i += 1

if sum == num:

    print(f"{num} is a perfect number.")

else:

    print(f"{num} is not a perfct number.")

