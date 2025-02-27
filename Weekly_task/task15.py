# wap that takes a string as input counts the frequency of each word in the string.

# Hello world! Hello Python. Python is great, isn't it?


def word_frequency(text):

    new = ""

    new2 = []

    for i in text:

        if i.isalnum() == True:

            new += i

        else:

            new += " "

    for i in new.split():

        if i not in new2:

            count = new.count(i)

            print(f"{i} : {count}")

            new2.append(i)



word_frequency("Hello world! Hello Python. Python is great, isn't it?")

