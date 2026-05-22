try:
    num1=int(input("enter number"))
    num2=int(input("enter number"))
    div=num1/num2
except ZeroDivisionError as e:
    print("number can not devided by zero")
    print(e.args) 

else:
    print(div)        
