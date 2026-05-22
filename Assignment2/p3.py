# Check the given character uppercase or lower case or digit or special
# character

given = input()
if given.islower():
    print("lower case")
elif given.isupper():
    print(" upper case")
elif given.isdigit():
    print("its a digit")
else:
    print("its special char")