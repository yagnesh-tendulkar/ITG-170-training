n=int(input("Enter n:"))
cou=0
num=2
while(cou<n):
    s=0
    for i in range(1,num):
        if(num%i==0):
            s+=i
    if(s==num):
        print(num,end=" ")
        cou+=1
    num+=1
