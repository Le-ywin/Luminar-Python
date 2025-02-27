# To check a word is a palindrome or not

# A palindrome is a word, phrase, number, or sequence of characters that reads the same forward as backward, ignoring spaces, punctuation, and capitalization.

text = input("Enter the word: ")

if text[::-1] == text:

    print("Yes sire, It is a palindrome")

else:

    print("Sire, I'm afraid it is not a Palindrome")

