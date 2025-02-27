# wap that converts a phrase into its abbreviation using the first letter of each word(ignoring small words like "and", "the", "of").

# i/p : National Aeronautics and Space Administration
# o/p : NASA

# i/p : World Health Organization
# o/p : WHO

# i/p : The United States of America
# o/p : USA

def abbreviation(string):

    new = ""

    for i in string.split():

        if len(i) > 3:

            new += i[0]

    print(new.upper())

abbreviation("National Aeronautics and Space Administration")