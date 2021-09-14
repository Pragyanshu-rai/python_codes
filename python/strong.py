string = input()

def isStrong(string):

    alpha = "abcdefghijklmnopqrstuvwxyz"

    for char in string:
        
        if char.lower() not in alpha:
            return False

    return True

if isStrong(string) and string == string[::-1]:
    print("you inputted a strong string.")

else:
    print("you inputted a weak string.")
