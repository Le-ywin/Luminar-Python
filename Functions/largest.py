# to check largest among 2 numbers

# def largest(a,b):

#     print(a if a > b else b)

# largest(4,2)

# to check largest among 3 numbers

def largest(a,b,c):

    print(a if a > b and a > c else b if b > a and b > c else c)

largest(5,3,4)