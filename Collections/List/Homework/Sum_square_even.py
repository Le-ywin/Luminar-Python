# wap to print the sum of square of even numbers of the list

numbers = [1,2,3,4,5,6,7,8,9,10]

sum = 0

product = 1

for i in numbers:

    if i % 2 == 0:

        product = i ** 2

        sum += product

print(sum)