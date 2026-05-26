m=int(input("Enter the number "))
n=int(input("Enter the number "))
for num in range(m, n+1):
    count=0
    temp1=num
    temp2=num
    while temp1>0:
        temp1=temp1//10
        count+=1
    sum=0
    while temp2>0:
        digit=temp2%10
        sum=sum+digit**count
        temp2=temp2//10
    if sum==num:
        print(num)