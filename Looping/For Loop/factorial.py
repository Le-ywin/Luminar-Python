# wap to find the facctorial of a number entered

num = int(input("Enter the No: "))

factorial = 1

for i in range(num,0,-1):

    factorial *= i

print(f"The factorial of the number is :{factorial}")