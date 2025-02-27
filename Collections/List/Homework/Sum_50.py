# wap to ask user to enter the number to a list until to the sum of numbers in list reach 50

list = []

sum = 0

# while(sum < 50):

#     num = int(input("Enter a No: "))

#     sum += num

#     if sum >= 50:

#         break

#     list.append(num)

# print(f"{list} and sum is {sum}")

for i in range(51):

    num = int(input("Enter a number: "))

    sum += num

    if sum >= 50:

        break

    list.append(num)

    print(list)

    print(sum)

print("The final list is: ", list)