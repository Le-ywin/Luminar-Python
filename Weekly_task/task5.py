# wap to print sum of even and odd indexed digits in a given number


number = input("Enter a No : ")

even,odd = 0,0

for i in number:

    if number.index(i) % 2 == 0:

        even += int(i)

    else:

        odd += int(i)

print(even,odd)