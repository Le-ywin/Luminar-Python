# wap to find the largest word in string without contains any vowel

text = input("Enter the text: ")

words = text.split(" ")

for i in words:

    for j in i:

        if j in "aeiou":

            break
    else:

        print(i)