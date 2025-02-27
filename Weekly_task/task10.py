# Write a function  that calculates the greatest common divisor (GCD) of two numbers a and b.

def gcd(x,y):

    divs1,divs2 = set(),set()

    for i in range(1,x+1):

        if x % i == 0:

            divs1.add(i)

    for j in range(1,y+1):

        if y % j == 0:

            divs2.add(j)

    print(max(divs1.intersection(divs2)))

gcd(20,10)