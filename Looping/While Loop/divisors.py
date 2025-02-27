# wap to find the divisors of the number entered by the user

num = int(input("Enter the No: "))

i = 1

while i < num:

    if num % i == 0:

        print(i)

    i += 1
