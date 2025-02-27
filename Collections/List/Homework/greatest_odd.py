# wap to find the greatest odd number from the list

numbers = [3,4,8,5,10,3,9,8,4,13]

greatest = numbers[0]

for i in numbers:

    if i > greatest and i % 2 != 0:

        greatest = i
    
print(f"The greatest odd number is: {greatest}")

