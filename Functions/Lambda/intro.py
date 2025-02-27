
# 3 o/p = 9

# def square(a):

#     print(a**2)

# square(3)

square = lambda num : num ** 2 # lambda anonymous function

print(square(3))

# lambda args : epression


# to find the square root of a number giveb

sqrt = lambda num : num ** 0.5

print(sqrt(16))


# add teo numbers

add = lambda a,b : a + b

print(add(3,4))


# write a function to check odd or even

oddeven = lambda a : ("Even" if a % 2 == 0 else "odd")

print(oddeven(4))