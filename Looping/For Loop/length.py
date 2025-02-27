# wap to find the length of string entered by user

name = input("Enter your name: ")

count = 0

for i in name:

    if " " in name:

        name = name.replace(" " , "")

    else:
        
        count += 1

print(count)