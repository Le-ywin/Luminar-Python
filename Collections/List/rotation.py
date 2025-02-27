numbers = [1,2,3,4,5,6,7]  # o/p => [5,6,7,1,2,3,4]

# while(numbers[0] != 5):
    
#     last = numbers.pop(6)
    
#     numbers.insert(0,last)

# print(numbers)

for i in range(3):

    last = numbers.pop(6)

    numbers.insert(0,last)

print(numbers)