#Check the given character uppercase or lower case or digit or special character?
char = input("Enter Character: ")
if char.isupper():
    print(char,"is Upper Case.")
elif char.islower():
    print(char,"is Lower Case.")
elif char.isdigit():
    print(char,"is Digit.")
else:
    print(char, "is Special Character.")