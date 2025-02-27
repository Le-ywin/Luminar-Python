
# Grade Selector

# Marks =

# Greater than 90 >> A grade

# Greater than 80 and less than or equal to 90 >> B grade

# Greater than 70 and less than or equal to 80 >> C grade

# Greater than 60 and less than or equal to 70 >> D grade

# Greater than or equal to 50 and less than or equal to 60 >> E grade

# less than 50 >> F grade

mark = int(input("Enter your marks: "))

if mark > 90:

    print("You got A Grade")

elif mark > 80 and mark <= 90:

    print("You got B Grade")

elif mark > 70 and mark <= 80:

    print("You got C Grade")

elif mark > 60 and mark <= 70:

    print("You got D Grade")

elif mark >= 50 and mark <= 60:

    print("You got E Grade")

else:

    print("Sorry, you failed the Exam, try again.")

