item1 = {"a":1,"b":2,"c":3}

item2 = {"a":4,"b":5,"c":6}

# result = {"a":[1,4],"b":[2,5],"c":[3,6]}

for i in item1:

    item1[i] = [item1[i],item2[i]]

print(item1)

