# wap to print a list of numbers n to m where n and m are entered by user

n = int(input("Enter the starting number: "))

m = int(input("Enter the ending number: "))

# list = []

# for i in range(n, m+1):

#     list.append(i)

# print(list)

print(list(range(n,m+1)))