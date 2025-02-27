# wap to print the duplicate elements

text = "welcome home"

i = 0

a = ""

while(i < len(text)):

    if text.count(text[i]) > 1 and text[i] not in a:

        print(f"{text[i]} is recursive and the count is {text.count(text[i])}")

        a += text[i]

    i += 1

