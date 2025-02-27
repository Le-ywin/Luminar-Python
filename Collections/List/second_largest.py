numbers = [124,84,21]

# num = max(numbers)

# numbers.remove(num)

# print(max(numbers))



# largest = 0

# for i in numbers:

#     if i > largest:

#         largest = i

# print(f"Largest is: {largest}")

# numbers.remove(i)

# largest = max(numbers)

# print(f"second largest is : {largest}")



largest = numbers[0]

second = numbers[1]

for i in numbers:

    if i > largest:

        second = largest

        largest = i

    elif i < largest and i > second:

        second = i

print(largest, second)