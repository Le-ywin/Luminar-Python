def perfect(num):

    div = []

    for i in range(1,num):

        if num % i == 0:

            div.append(i)

    print(f"{num} is a perfect number" if sum(div) == num else f"{num} is not a perfect number")

perfect(28)