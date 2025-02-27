# wap to find the first duplicate element in the list

numbers = [1,4,2,3,5,1,3,6,7]

for i in numbers:

    if numbers.count(i) != 1:

        print(f"The first duplicate element is : {i}")

        break
