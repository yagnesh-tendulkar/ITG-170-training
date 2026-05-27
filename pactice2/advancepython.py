try:
    num = int(input("Enter a number : "))
    divv = int(input("Enter a number to divide the num : "))

    res=num/divv
except ZeroDivisionError:
    print("Enter a non zero number...")
except ValueError:
    print("Enter a vaild number to execute....")
else:
    print("The resultant number is : ",res)
finally:
    print("program completed")