def prime(a):

    if a == 1:

        print("Enter a number greater than 1!")

    else:

        for i in range(2,int(a ** 0.5 + 1)):

            if a % i == 0:

                print(f"{a} is not prime")

                break

        else:

            print(f"{a} is prime")

prime(1)