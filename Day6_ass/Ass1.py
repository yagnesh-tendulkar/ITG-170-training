#Write a program to handle exceptions with Try-Catch Block.
try:
    num1=int(input("Enter a number:"))
    num2=int(input("Enter a number:"))
    result= num1/num2
    print("Result:",result)
except ZeroDivisionError as e:
    print("Cannot divide by zero.")