def isArmstrong(n):
    total=0
    num=n
    count=len(str(n))
    while num>0:
        rem = num%10
        total = total + rem ** count
        num=num//10
    return total==n

for i in range(1,1001):
    if isArmstrong(i):
        print(i)
