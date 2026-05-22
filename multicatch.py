try:
    number=int(input("enter number "))
    number2=int(input("enter number 2 "))
    res=number/number2
except  ZeroDivisionError as e:
    print(e.args)
except ValueError as v:
    print(v.args)
else :
    print(res) 
finally:
    print(" it is finally block")            
