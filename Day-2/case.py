
ch = input("Enter a character: ")

if ch.isupper():
    print("Uppercase Letter")
elif ch.islower():
    print("Lowercase Letter")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")
