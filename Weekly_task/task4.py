"""

wap to print the characters of a string in even positions. >>> name= "python"

o/p = y h n

"""

name = "python"

j = 1

for i in name:

    # if name.index(i) % 2 == 0:

    #     print(i)

    if j % 2 == 0:

        print(i)
    
    j += 1