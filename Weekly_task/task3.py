"""

wap to find the prime numbers below n where n is entered by user

"""


n = int(input("Enter the limit: "))

for i in range(2, n):

    for j in range(2, int(i**0.5) + 1):

        if i % j == 0:

            break

    else:

        print(i)
