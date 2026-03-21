#finish ext

"""
4. Password reset program

Only accept a new password if it is:
    At least eight characters long
    Has lower case and upper case letters.

The password reset program should also make the user input their new password twice so that the computer knows that the user has not made any mistakes when typing their new password.
Extensions:
    Make some sort of algorithm to suggest how strong the password is (Weak, Medium, Strong) depending on length, whether or not the password has special characters in etc
    Let the user input their username. The program should go to a text file with a list of usernames and old passwords, and the program should only let you change your password if you input your old password.
"""

specialChars = ['!','"','£','$','€','%','^','*','(',')','+','=','-','_','/',',','<','>','.',':',':',':','@','#','#','|','¬','`','¦']
uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

while True:
    password = input("Please enter your password: ")
    password2 = input("Please re-enter your new password: ")

    if len(password) < 8: # checks if pass long enough
        print("Password must have over 8 characters")
    else:
        if not any(i in lowercase for i in password): # tried using for loop but would print loads of times
            print("Password must contain a lowercase letter") # read documentation for any()
            continue

        if not any(i in uppercase for i in password):
            print("Password must contain a capital letter")
            continue

        if password != password2: # checks if pass the same as pass2
                print("Passwords dont match")
        else:
            break

if any(i in specialChars for i in password):
    print("Password strength: Strong")
else:
    print("Password strength: Weak")

print("Password has sucessfully been changed")
