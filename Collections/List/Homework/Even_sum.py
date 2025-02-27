# wap to find the sum of even numbers in a given list

numbers = [1,2,3,4,5,6,7,8,9,10]

sum = 0

for i in numbers:

    if i % 2 == 0:

        sum += i

print(sum)
