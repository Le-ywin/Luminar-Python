numbers = [1,2,3,4,5,6]

# sum = 0

# for i in numbers:

#     if i % 2 == 0:

#         sum += i

# print([sum])

print([sum([i for i in numbers if i % 2 == 0])])

