ch = input("Enter a character: ")
if ch.isupper():
    print("The character entered is uppercase")
elif ch.islower():
    print("The character entered is lowercase")
elif ch.isdigit():
    print("The character entered is digit")
else:
    print("The character is a special character")