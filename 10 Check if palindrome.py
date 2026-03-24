"""10. Check if palindrome
    Checks if the string entered by the user is a palindrome.
"""

word = input("Word: ")

word2 = word[::-1]
if word == word2:
    print("Yes it is a palindrome")
else:
    print("No its not a palindrome")