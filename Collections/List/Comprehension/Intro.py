# List comprehension in Python is a concise and elegant way to create lists.

# new_list = [expression for item in iterable if condition]



numbers = [1,2,3,4,5,6,7]

# even = []

# for i in numbers:

#     if i % 2 == 0:

#         even.append(i)

# print(even)

# even = [i for i in numbers if i % 2 == 0]

# print(even)


print([i ** 2 for i in numbers if i % 2 != 0])

