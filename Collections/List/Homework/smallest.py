# wap to find the smallest element in the list

numbers = [4,6,2,12,5,7,4,3,9,1]

smallest = numbers[0]

for i in numbers:

    if i < smallest:

        smallest = i

print(smallest)


# smallest = min(numbers)


# numbers.sort()

# print(f"smallest is {numbers[0]}")