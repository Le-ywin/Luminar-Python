"""
    Given a pattern text=”ABEABAIACB”
   Write a program to print most recursive consonant from above text 
   Output=B

"""

pattern = "ABEABAIACB"

most = 0

cons = ""

for i in pattern:

    if i not in "aeiouAEIOU" and pattern.count(i) > most:

        most = pattern.count(i)

        cons = i

print(cons)