
# o/p = yhn   odd index number element

# text = "python"

# for i in text:

#     if text.index(i) % 2 != 0:

#         print(i,end = '')



text = "python"

result = ""

for i in text:

    if text.index(i) % 2 != 0:

        result += i                        # using concatination

print(result)

