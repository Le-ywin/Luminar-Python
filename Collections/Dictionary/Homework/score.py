"""

Make a dictionary of student names and their scores.(5 element)

>> find the highest score
>> find the smallest score

sample dictionary format : {"arun":98,"a":78,"b":64}

arun , a,b

"""

details = {"Arthur Leywin" : 99,"Nico" : 89,"Tessia Heralith" : 95,"Evelyn" : 85,"Grey" : 100}

# smallest = "Arthur Leywin"

# highest = "Arthur Leywin"

# for i in details:

#     if details[i] > details[highest]:

#         highest = i

#     elif details[i] < details[smallest]:

#         smallest = i

# print(f"{highest} got the highest score of {details[highest]}")

# print(f"{smallest} got the smallest score of {details[smallest]}")



largest = 0

smallest = 100

for name in details:

    smallest = min(smallest,details[name])

    largest = max(largest,details[name])

print(smallest)

print(largest)