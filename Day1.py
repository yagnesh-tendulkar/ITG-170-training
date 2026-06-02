# Program 1 : Print Personal Details using Variables
name = "Vennela"
city = "Nellore"
date = "11-05-2026"
favorite = "Dance"

print(f"My name is {name}")
print(f"My city is {city}")
print(f"Today's date is {date}")
print(f"My favorite thing is {favorite}")

# Program 2 : Arithmetic Operations

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Sum =", num1 + num2)
print("Difference =", num1 - num2)
print("Product =", num1 * num2)
print("Division =", num1 / num2)

# Program 3 : Different types of strings

single = 'This is single quote string'
double = "This is double quote string"
triple = """This is
triple quote
string"""

print(single)
print(double)
print(triple)

# Program 4 : Greatest Number

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is greater")
elif b > a:
    print(b, "is greater")
else:
    print("Both are equal")

# Program 5 : Multi - line Introduction

intro = """
My name is Vennela Padiginati.
Recently i have completed my masters.
Currently working as a software trainee in Miracle Software Systems.
"""

print(intro)

# Program 6 : Book Bill Calculation
price = 250
quantity = 5
total = price * quantity

print(f"Price of one book = {price}")
print(f"Quantity = {quantity}")
print(f"Total cost = {total}")

# Age Calculation

birth_year = int(input("Enter your birth year: "))
current_year = 2026

age = current_year - birth_year

print("Your age is:", age)

# Name Operations

name = input("Enter your name: ")

print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Length:", len(name))

# Celsius to Fahrenheit conversion

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit =", fahrenheit)