"""
Write a function  that reverses the order of words in a given sentence but keeps the characters in each word in the correct order.
Example: "Hello World" → "World Hello"
"""

def rev(string):

    new = string.split(" ")[::-1]

    for i in new:

        print(i,end=" ")

rev("hello hi")