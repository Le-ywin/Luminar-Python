d1 = {"name" : "hari","age" : 24,"job" : "trainer","place" : "kochi"}

d2 = {"job" : "Team lead","place" : "kakkanad","salary" : 10000}

# o/p = d1 = {"name" : "hari","age" : 24,"job" : "Team lead","place" : "kakkanad"}


# for i in d1:

#     for j in d2:

#         if i == j:

#             d1[i] = d2[j]

# print(d1)

for i in d1:

    if i in d2:

        d1[i] = d2[i]

print(d1)