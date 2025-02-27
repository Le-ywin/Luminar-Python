word = input("Enter the word: ")

count = 0

j = ""

for i in word:

    if i in "aeiou" and i not in j:

        print(f"{i} is a vowel")

        j = j + i

