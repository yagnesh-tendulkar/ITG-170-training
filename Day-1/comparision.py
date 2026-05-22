string1 = 'Neema'
string2 = "Reetu is dumb"
string3 = """i love Sumathi"""

print("Single Quotes String:", string1)
print("Double Quotes String:", string2)
print("Triple Quotes String:", string3)


num1 = float(input("Sumathi please enter first number: "))
num2 = float(input("Sumathi please enter second number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print("Both numbers are equal")
