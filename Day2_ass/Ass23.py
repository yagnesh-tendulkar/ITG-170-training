#Program to print perfect numbers between m to n.
m=int(input("Enter a number from where to start:"))
n=int(input("Enter a number from where to end:"))

for i in range(m,n+1):
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum=sum+j
    if sum==i:
        print(i)
        
