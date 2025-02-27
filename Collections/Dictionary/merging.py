
key = ["name","place","position"]

values = ["vinay","kochi","trainer"] # ("name" : "vinay",:place : "kochi","position" : "trainer")

new = {}

# i = 0

# while i < 3:

#     new[key[i]] = values[i]

#     i += 1

# print(new)

for i in range(len(key)):

    new[key[i]] = values[i]

print(new)

