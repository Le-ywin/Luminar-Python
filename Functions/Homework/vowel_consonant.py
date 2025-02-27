# Write a function count_vowels_consonants(string) to count the vowels and consonants in a string.

def count_vowels_consonants(string):

    vowel = 0

    consonants = 0

    for i in string:

        if i in "aeiou":

            vowel += 1

        else:

            consonants += 1

    print(f"The string has {vowel} vowels and {consonants} consonants.")

count_vowels_consonants("With aether, I could rewrite reality itself, it was only a matter of learning how . Then these gods would see what I was really capable of.")

