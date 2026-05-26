n=int(input("Enter the given number "))
sum=0
fact=0
for i in range(1,n+1):
    fact=fact*i
    sum=sum+(1/fact)
print(sum)