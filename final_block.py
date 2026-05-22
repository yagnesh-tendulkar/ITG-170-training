try:
    num1=int(input("enter num1 value:"))
    num2=int(input("enter the num2 value:"))
    print(num1/num2)
except ZeroDivisionError:
    print("cant divide by zero")
finally:
    print("successfully executed the program")
    