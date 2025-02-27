# wap to find the product of numbers in a digit

num = int(input("Enter the digit: "))

product = 1

for i in str(num):

    product *= int(i)

print("Product of digits is: ", product)