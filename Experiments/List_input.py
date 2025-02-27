

n = int(input("How many input dou you want to add: "))

list = []

for i in range(n):

    list.append(input(f"Enter item : "))
    
    # list += [input("Enter item: ")]

list.sort()

list.reverse()

print(list)