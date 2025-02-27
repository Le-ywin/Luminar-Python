# wap to find the prime numbers from the list

numbers =[1,3,7,5,11,9,30,12]

prime = []

for i in numbers:

    for j in range(2,i):

        if i % j == 0:

            break

    else:
        if i == 1:

            continue
        
        prime.append(i)

print(f"{prime}")