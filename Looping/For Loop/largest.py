# Python is a popular programming language

# wap to find the largest word from the above string

text = "Python is a popular programming language"

largest = 0

for i in text.split(" "):

    if len(i) > largest:

        largest = len(i)

        element = i

print(f"The word - {element} - is the largest word ({largest})")