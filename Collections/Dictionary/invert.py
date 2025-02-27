items = {"a":1,"b":2,"c":3}

# o/p = {1:"a",2:"b",3:"c"}

new = {}

for i in items:

    new[items[i]] = i  # new[1] = "a"

print(new)

