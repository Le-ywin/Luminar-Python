# wap to find the smallest even number from the list

numbers = [1,2,3,4,5,6,7,8,9,10]

# smallest = 10

# for i in numbers:

#     if i < smallest and i % 2 == 0:

#         smallest = i

# print(f"The smallest even number is {smallest}")


numbers.sort()

for i in numbers:

    if i % 2 == 0:

        print(i)

        break