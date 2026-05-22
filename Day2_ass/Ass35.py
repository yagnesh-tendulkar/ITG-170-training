#Program to check whether a given number is a happy number or not?
num=int(input("Enter a number:"))
while num!=1 and num!=4:
    sum=0
    while num>0:
        rem=num%10
        sum=sum+(rem*rem)
        num=num//10
    num=sum

if sum==1:
    print(num,"is a happy number.")
else:
    print(num,"is not a happy number.")

