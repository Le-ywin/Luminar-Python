"""

File handling in python involves operations such as creating, reading, writing, and closing files, utilizing various modes to manage data.

read()   "r"

write()     "w"

append()    "a"

open("filename","r)

"""

# file = open("text.txt","r")

# print(file.read())

# file = open("new.txt","w") # existing file content overwrite | non existing new file create

# file.write("Arthur Leywin")

# file = open("new.txt","a")

# file.write(" From Dicathen")



# file = open("new.txt","r")

# result = file.read()

# result = result.split()

# print(len(result))



# file = open("new.txt","r")

# result = file.read().split()

# n = input("Enter the word: ")

# if result.count(n) < 1:

#     print("Word does not exist.")

# else:
    
#     print(result.count(n))

# # print()



# file = open("new.txt","r")

# print(list(set(file.read().split())))



# file = open("/home/ram/Luminar/File Handling/teask.txt","w")

# file.write("Arthur Leywin")



# file = open("text.txt","r")

# print(file.readline())   # only reads the first line in the file

# print(file.readlines())  # each line represent as a element in a list

# print(file.readable())     # Whether file was able to read (True/False)



# with open("text.txt","r") as file:

#     print(file.read())

# file.close() | with >> it ensures file closing right after proccessing them



# with open("text.txt","r") as a:

#     new1 = open("new1.txt","w")

#     new1.write(a.read())



# with open("text.txt","r+") as a:

#     print(a.read())

#     a.write("\nRegis")


"""
hari 60 78 90
amal 80 98 76
aswin 90 98 71
"""

