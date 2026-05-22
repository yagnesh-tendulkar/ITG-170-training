number=int(input("enter your number ?"))
flag=True
digit=number%10
while(number!=0):
    rem=number%10
    if(digit!=rem):
        flag=False
        break
    digit=rem
    number=number//10
if(flag):
    print(" all digits are equal")
else:
    print("all digits are not equal")    