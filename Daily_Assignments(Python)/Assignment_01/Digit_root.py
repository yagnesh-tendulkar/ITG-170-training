# Prints digit root of given Number

input_number = int(input("Enter a number: "))
digit_root = 9 if input_number % 9 == 0 else input_number % 9

print("Digit root is:", digit_root)