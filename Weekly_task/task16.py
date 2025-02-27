# wap to read a user input 

# input string = "pneumonoultramicroscopiesilicovolcano"

# display the vowel count

# display the consonant count

def count(string):

    vowel = 0

    consonants = 0

    for i in string.lower():
        
        if i in "aeiou":

            vowel += 1

        else:

            consonants += 1

    print(f"Vowels : {vowel}, Consonants : {consonants}")

count("pneumonoultramicroscopiesilicovolcano")