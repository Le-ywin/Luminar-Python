# Exception Handling / Error Hndling
# ==================================


# Python exception handling manages runtime errors using try-except blocks to prevent crashes and handle errors gracefully.

"""
Exception Handling in Python allows you to manage errors that occur during program execution.
This prevents your program from crashing and gives you control to respond appropriately when errors arise.
"""


try:

    a = int(input("Enter the No: "))

    b = int(input("Enter The No: "))
    
    result = a / b

    print(result)

except ZeroDivisionError:

    print("Division by Zero is not possible")

except ValueError:

    print("Enter a Number!")