# wap to enter a list of integers

# 1) try to convert all the elements in the list to int

# 2) try to pick a element from a specific index




# numbers = [1,2,"3",4,"hi","5","abc"]

# new = []

# try:

#     for i in numbers:

#         i = int(i)

#         new.append(i)

# except ValueError:

#     print("Please enter a list of numbers!")

# print(new)


new = [1,"Arthur",3,"Leywin",5,6,7,"hi"]

index = int(input("Enter a index number :"))

try:

    print(new[index])

except IndexError:

    print("Index out of range")
