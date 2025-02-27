"""

Ask to enter a number, if it is under 10 display "too low",
if it is between 10 and 20(inclusive) display "correct",
if it is over 20 display "too high".

"""

num = int(input("Enter a number: "))

if num < 10:

    print("Too Low")

elif num >= 10 and num <= 20:

    print("Correct")

else:

    print("Too High")

