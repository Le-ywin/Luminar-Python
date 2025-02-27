
# missing number from a sequence of numbers

numbers = [6,8,9,4,7]

for i in range(min(numbers), max(numbers)):

    if i not in numbers:

        print(f"{i} is the missing number")
