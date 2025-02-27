items = {"a":1,"b":2,"c":1,"d":3,"e":2}  # remove keys with duplicate values

var = []

for i in items.copy():

    if items[i] in var:

        items.pop(i)

    else:

        var.append(items[i])

print(items)