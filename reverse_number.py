number=int(input("enter the number ? "))
res=0
while(number!=0):
    rem=number%10;
    res=res*10+rem
    number=number//10
print(res)    