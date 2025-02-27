# Regular Expressions
# ===================

# Regular expressions are patterns used to match character combination in strings.

# Validating a password

# match(pattern,string) -> check if the pattern in the beginning of string

# search(pattern,string) -> check the pattern anywhere in tvhe string

# fullmatch(pattern,string) -> find all occurences of pattern in the string

# finditer(pattern,string) -> returns the position of pattern in the string

import re

# string = "python is a programming language"

# pattern = "python"

# print(re.search(pattern,string))

# if re.match(pattern,string):

#     print("Match found")

# else:

#     print("Match not found")





# text = "python is a program"

# pattern = "program"

# result = re.search(pattern,text)

# if result:

#     print(result.group(),[result.start(),result.end()])

#     # print([result.start(),result.end()])





# string = "python is a programming language, python used to build backend"

# pattern = "python"

# # match = re.findall(pattern,string)    # Return a list of all pattern matches in the string.

# # print(match)


# match = re.finditer(pattern,string)

# for i in match:

#     print([i.start(),i.end()],i.group())





# text = "KL 31 AT 0707"

# pattern = r'KL\s[0-9]{2}\s[A-z]{1,2}\s[0-9]{4}'

# # pattern = r'^kl\s[0-9]{2}\s[a-z]{1,2}\s[0-9]{4}$'        # ^ -> start of string, $ -> end of string

# result = re.match(pattern,text)

# if result:
    
#     print("Validated")

# else:

#     print("Not valid")





# wap to validate gmail id

# text = "true.leywin@gmail.com"

# pattern = r'[A-z0-9.-]+@gmail.com'

# result = re.match(pattern,text)

# if result:

#     print("Valid")

# else:

#     print("Not valid")





# wap to validate mobile number


# number = "+91 8111854219"

# pattern = r'(?:\+91|91)\s?[6789][0-9]{9}'

# result = re.match(pattern,number)

# if result:

#     print("Valid")

# else:

#     print("Not valid")




"""

Username,
Can contain only letters (a-z, A-Z), digits (0-9), and underscores (_).
Must start with a letter.
Length should be between 4 to 15 characters.

"""

# name = "Arthur_Leywin_"

# pattern = r'^[A-z][A-z0-9_]{3,14}$'

# result = re.match(pattern,name)

# if result:

#     print("Valid")

# else:

#     print("Not valid")