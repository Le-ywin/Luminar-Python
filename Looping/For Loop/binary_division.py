num = int(input("Enter the No: "))

bin = ""

while num > 0:

    rem = num % 2

    num = num // 2

    bin = bin + " " + str(rem)

print(bin[::-1])

"""4 = 4 % 2 = 0, 4 // 2 = 2

2 % 2 = 0, 2 // 2 = 1

1 % 2 = 1, 1 // 2 =0"""