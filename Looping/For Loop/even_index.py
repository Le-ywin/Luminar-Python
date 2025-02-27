# wap to print the element in even index position of the string

text = input("Enter the text: ")

for i in text:

    if text.index(i) % 2 == 0:

        print(i)