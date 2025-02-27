# text = "python"  # o/p = "npytho"

# temp = text[-1] + text[0:-1]

# print(temp)

text = "hellopython"  # o/p = "ollehpython"

if "p" in text:

    temp = text[0:text.index("p")]

    print(temp[::-1] + text[text.index("p")::])   #temp[::-1] >> used to reverse the string

else:

    print("Sorry, you cannot proceed")

