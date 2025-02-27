items = {2:8,4:6,7:9,1:2}

# [10,10,16,3]

# new = []

# for i in items:

#     num1 = i

#     num2 = items[i]

#     sum = num1 + num2

#     new.append(sum)

# print(new)


# for i in items:

#     new.append(i + items[i])

# print(new)


print([i+items[i] for i in items])