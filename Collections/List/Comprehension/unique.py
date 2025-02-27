# text = "abcbcdedf"

# list = []

# for i in text:

#     if text.count(i) == 1:

#         list.append(i)

# print(list)

# print([i for i in text if text.count(i) == 1])

text = "pythonlanguage"


unique = []

for i in text:

    if i not in unique:

        unique.append(i)

print(unique)