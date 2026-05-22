#Program to whether all digits in a given number are equal or not?
num=int(input("Enter a number: "))
digit=num%10
equal=True
while num>0:
    rem=num%10
    if rem!=digit:
        equal=False
        break
    num=num//10
    
if digit==rem:
    print("All are equal.")
else:
    print("All are not equal.")