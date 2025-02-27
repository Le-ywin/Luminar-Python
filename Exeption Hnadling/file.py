# wap that reads a file and read the content. it should handle the exception

try:

    file = open("abc.txt","r")

    result = file.read()

    print(result)

except FileNotFoundError:

    print("Enter a Existing ile name")

