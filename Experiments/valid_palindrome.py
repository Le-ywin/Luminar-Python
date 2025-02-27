# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

s = "A man, a plan, a canal: Panama"

a = ""

for i in s:

    if i.isalpha():

        a+=i

a = a.lower()

print("Palindrome" if a == a[::-1] else "Not palindrome")