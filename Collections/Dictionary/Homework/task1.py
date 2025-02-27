keys = ["orange","apple","kiwi","grape","banana"]

value = ["hello","hai"]

# o/p = {"orange" : "hello","apple" : "hai","kiwi" : 1,"grape" : 2,"banana" : 3}

new = {}

j = 1

for i in range(len(keys)):

    while(len(value) < len(keys)):

        value.append(j)

        j += 1

    new[keys[i]] = value[i]

print(new)




# keys = ["orange", "apple", "kiwi", "grape", "banana"]

# value = ["hello", "hai"]

# new = {}

# value.extend(range(1, len(keys) - len(value) + 1))

# for i in range(len(keys)):

#     new[keys[i]] = value[i]

# print(new)
