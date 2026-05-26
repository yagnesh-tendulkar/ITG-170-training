n=int(input("Enter the n value "))
sum=0
power=0
for i in range(1,n+1):
    sum=sum+(1/i**power)
    power+=1
print(sum)