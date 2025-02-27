from functools import reduce

numbers = [4,1,5,6,7,8,10,3,7]

# apply a function to double each element

# then extract the numbers greater than 10 and take the product of numbers

double = map(lambda a : a * 2,numbers)

# print(list(double))

greater = filter(lambda a : a > 10,double)

print(reduce(lambda a,b:a*b,greater))

