# wap to check a nmber is palindrome or not

num = int(input("Enter the No: "))

temp = num

sum = 0

while(temp > 0):

    value = temp % 10

    sum = sum * 10 + value

    temp //= 10

if num == sum:

    print(f"{num} is a palindrome")

else:

    print(f"{num} is not a palidrome")