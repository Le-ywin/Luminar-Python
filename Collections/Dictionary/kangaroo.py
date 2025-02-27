
text = "radioactive"

word = input("Enter the word: ")

new = {}

for i in text:

   new[i] = text.count(i)

print(new)

for j in word:

    if j in text and new[j] > 0:

        new[j] -= 1

    else:

        print("Not a kangaroo")

        break
    
else:

    print("Kangaroo")