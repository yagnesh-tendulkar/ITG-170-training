#Program to Find the Sum of the Series 1/1+1/4+1/9+…1/N^2
num=int(input("Enter a number:"))
sum=0
for i in range(1,num+1):
    sum=sum+(1/(i*i))
print(sum)