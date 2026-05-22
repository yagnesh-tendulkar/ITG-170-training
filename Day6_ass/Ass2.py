#Write a program to handle exceptions with Multiple Catch Block.
try:
    n1=int(input("Enter a number:"))
    n2=int(input("Enter a number:"))
    result=n1/n2
    print("Result:",result)
except ZeroDivisionError:
    print("cannot divide by 0")
except ValueError:
    print("Enter correct value.")

