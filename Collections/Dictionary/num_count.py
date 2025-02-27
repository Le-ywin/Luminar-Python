items = [1,2,2,3,3,3,4,4,4,4]

# o/p = {1:1,2:2,3:3,4:4}

new = {}

for i in items:
        
    new[i] = items.count(i)

print(new)
