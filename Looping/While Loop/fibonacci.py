num = int(input("Enter the limit: "))

i = 2

a = 0

b = 1

print(a)

print(b)

while( i < num):

    c = a + b

    print(c)

    a,b = b,c

    i += 1