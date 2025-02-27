# wap to find the number vowels in the string

# text = "hellopython"

# i = 0

# vowels = 0

# while i < len(text):

#     if text[i] in "aeiou":

#         vowels += 1

#     i += 1

# print(vowels)


# wap to find the number of vowels in the string and print the count of each vowels

text = "hellopython"

i = 0

a = ""

while i < len(text):

    if text[i] in "aeiou" and text[i] not in a:

        print(f"{text[i]} is a vowel and has a count of {text.count(text[i])}")

        a += text[i]

    i += 1

