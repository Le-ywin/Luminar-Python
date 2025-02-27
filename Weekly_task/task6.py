# Write a function that returns a list of all divisors of n.

def divisors(n):

    divs = []

    for i in range(1,n):

        if n % i == 0:

            divs.append(i)
        
    print(divs)


divisors(10)