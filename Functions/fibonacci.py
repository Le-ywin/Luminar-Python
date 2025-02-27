# recursive function

# functions that call itselt. it is always made up of 2 portions, the base case and recursive case


def fibonacci(n):

    if n == 0:

        return n
    
    elif n == 1:

        return n
    
    elif n > 1:

        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(4))
    
n = int(input("Enter the value: "))

for i in range(n):

    print(fibonacci(i))