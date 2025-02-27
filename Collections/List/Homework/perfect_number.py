# wap to find the perfect numbers from the list

numbers = [4,2,6,7,9,3,28,]

perfect_numbers = []

for num in numbers:

    sum = 0

    for i in range(1,num):

        if num % i == 0:

            sum += i

        if sum == num:

            perfect_numbers.append(num)

            break

print(f"The percfect numbers from the list : {perfect_numbers}")