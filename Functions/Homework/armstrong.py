def armstrong(number):

    arm = 0

    number = (str(number))

    for i in number:

        temp = int(i) ** len(number)

        arm += temp

    print(f"{number} is an armstrong" if arm == int(number) else f"{number} is not an armstrong")

armstrong(153)

# def armstrong(num):

#     print(f"{num} is an armstrong number" if sum(int(i) ** len(str(num)) for i in str(num)) == num else print(f"{num} is not an armstrong"))

# armstrong(153)
