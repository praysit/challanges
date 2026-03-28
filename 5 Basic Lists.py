"""
5. Asks for names until the user wants to print the list either reversed or in order.
"""

names = []

while True:
    name = input("Please add a name to the list: ")

    if name.lower() == "stop":
        ans = input("Do you want to print the list in order? ")
        if ans.lower() == "yes":
            print(list(reversed(list)))
        elif ans.lower() == "no":
            print(names)
        else:
            print("Please say either 'yes' or 'no'")
        break
    else:
        names.append(name)