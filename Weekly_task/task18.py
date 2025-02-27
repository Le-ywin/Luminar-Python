# wap which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a coma-seperated sequence on a single line

# o/p : 2000,2002,2004,2006,...

for i in range(1000,3001):

    for j in str(i):

        if int(j) % 2 != 0:

            break

    else:

        print(i)