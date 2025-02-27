#  wap to find the sum of digits in a number

num = int(input("Enter a No: "))

sum = 0

for i in range(num):

    temp = num % 10

    sum += temp

    num //= 10

print(f"The sum of the digit is: {sum}")