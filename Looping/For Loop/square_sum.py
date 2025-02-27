# find the sum of square of n natural numbers

limit = int(input("Enter the limit: "))

sum = 0

for i in range(1,limit+1):

    temp = i * i

    sum += temp

print(f"The sum os square of n natural numbers is: {sum}")