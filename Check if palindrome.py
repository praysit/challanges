word = input()

word2 = word[::-1]
if word == word2:
    print("Yes it is a palindrome")
else:
    print("No its not a palindrome")