"""

A Harshad number is an integer that is divisible by the sum of its digits.
when you add up all its digits and divide the original number by that sum,
the result is an integer.
For example, 18 is a Harshad number since 18 / (1+8)

"""

num = int(input("Enter the No: "))

sum = 0

temp = num

for i in str(num):

    sum += int(i)

if num % sum == 0:

    print(f"{num} is a Harshad Number")

else:

    print(f"{num} is not a Harshad Number")