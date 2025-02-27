input = input("Enter the word: ") # o/p = {"p":1,"r":2,"o":1,"g":2,"a":1,"m":2,"i":1,"n":1}

new = {}

# var = ""

# for i in input:

#     count = 1

#     if i in var:

#         count += 1

#     var += i

#     new[i] = count

# print(new)


for i in input:

    new[i] = input.count(i)

print(new)