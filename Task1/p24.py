n=int(input("Enter the n value "))
for num in range(n+1):
    sum=0
    for i in range(1,num):
        if(num%i==0):
            sum+=i
    if sum==num:
        print(num)
