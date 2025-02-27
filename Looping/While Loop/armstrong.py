"""

wap to check a number is armstrong or not

armstrong example

153

1^3 + 5^3 + 3^3 == 153

"""

num = int(input("Enter the No: "))

temp = num

length = len(str(num))

sum = 0

while(temp > 0):

    value = temp % 10

    value **= length

    sum += value

    temp //= 10            #

if num == sum:

    print(f"{num} is an armstrong number.")

else:

    print(f"{num} is not an armstrong number.")