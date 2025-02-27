# wap to print the count of vowels from a string

word = input("Enter the word: ")

count = 0

for i in word:

    if i in "aeiou":

        count += 1

print(count)