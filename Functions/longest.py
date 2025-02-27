def longest(text):

    longest = 0

    for i in text.split(" "):

        if len(i) > longest:

            longest = len(i)

            word = i
        
    print(word)

longest("The Beginning After The End")