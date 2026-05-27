n=int(input("Enter n:"))
sum=0
for i in range(1,int(n/2) + 1):
    if(n%i==0):
        sum+=i
if(sum==n):
    print(n,"is a Perfect Number")
else:
    print(n,"is not a Perfect Number")

