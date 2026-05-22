ch = input("Enter a character: ")

if ch.isupper():
    print("Uppercase character")

elif ch.islower():
    print("Lowercase character")

elif ch.isdigit():
    print("Digit")

else:
    print("Special character")