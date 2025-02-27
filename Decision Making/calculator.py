
print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division")

c = int(input("Select an operation: "))

a = int(input("1st Digit :"))

b = int(input("2nd Digit :"))

if(c == 1):

    print(a + b)

elif(c == 2):

    print(a - b)

elif( c == 3):

    print(a * b)

elif( c == 4):

    print( a / b)

else:

    print("Invalid Selection!!!")