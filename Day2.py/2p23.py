m=int(input("Enter m:"))
n=int(input("Enter n:"))
for i in range(m+1,n):
    sum=0
    for j in range(1,i):
        if(i%j==0):
            sum+=j
    if(sum==i):
        print(i,end=" ")