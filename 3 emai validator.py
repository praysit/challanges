#finish length checks and ext

"""
3. Email validator

Make a program to check whether an email address is valid or not.

For instance, you could make sure that there are no spaces, that there is an @ symbol and a dot somewhere after it. Also check the length of the parts at the start, and that the end parts of the address are not blank.
Extensions:

    When an email address is found to be invalid, tell the user exactly what they did wrong with their email address rather than just saying it is invalid.
    Allow the user to choose to give a text file with a list of email addresses and have it process them all automatically.
"""

""" old code
email = input("Please enter your email: ")

if " " in email:
    print("Email must not contain spaces")
else:
    if "@" not in email:
        print("Email must have an @")
    else:
        if "." not in email:
            print("Email must have a fullstop")
        else:
            print("All good!")
            
"""
valid = True
email = input("Please enter your email: ")

if " " in email:
    valid = False
    print("Email mustn't contain spaces")

if "@" not in email:
    valid = False
    print("Email must contain an @")

if "." not in email:
    valid = False
    print("Email must contain a fullstop")

if valid:
    print("Passed")
else:
    print("Failed")





