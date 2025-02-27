# def divisors(num):

#     div = []

#     for i in range(1,num):

#         if num % i == 0:

#             div.append(i)

#     print(div)

# divisors(10)

def divisors(num):

    print([i for i in range(1,num) if num % i == 0])

divisors(10)