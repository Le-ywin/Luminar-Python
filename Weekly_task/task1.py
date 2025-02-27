"""

Given a pattern
 Text=”ABABC”
 Write a program to print first non-recursive character output=c without using nested loop
 
"""


text = "ABABC"

new = []

# for i in text:

#     if text.count(i) == 1:

#         print(f"{i} is the 1st non recursive character")


print([f"{i} is the 1st non recursive character" for i in text if text.count(i) == 1])
