ch = input("Enter a character: ")

if ch.isupper():
    print("Uppercase Character")

elif ch.islower():
    print("Lowercase Character")

elif ch.isdigit():
    print("Digit")

else:
    print("Special Character")