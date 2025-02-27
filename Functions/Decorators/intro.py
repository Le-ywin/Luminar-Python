# DECORATOR

# Funtions that modify the behavior of other functions, classes, or methods
# without modiying it's structure

def swap(fn):

    def wrapper(a,b):

        if b == 0:

            a,b = b,a
        
        return fn(a,b)
    
    return wrapper

@swap
def division(a,b):

    print(a/b)

division(8,2)

division(4,0)