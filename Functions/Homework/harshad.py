def harshad(num):

    temp = sum(int(i) for i in str(num))

    print("harshad" if num % temp == 0 else "not harshad")

harshad(18)