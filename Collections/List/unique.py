numbers = [1,8,3,7,5,10,1,4,3]

list = []

# for i in numbers:

#     if numbers.count(i) > 1:

#         list.append(i)

#         numbers.pop(numbers.index(i))

# numbers.sort()

# print(numbers)

for i in numbers:

    if i not in list:

        list.append(i)

list.sort()

print(list)