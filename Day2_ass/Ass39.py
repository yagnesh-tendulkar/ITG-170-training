#Program to Find the Sum of the Series 1/2^0+1/2^1+1/2^2+1/2^3+1/2^4.
num=int(input("Enter a number:"))
sum=0
for i in range(num):
    sum=sum+(1/(2**i))
print(sum)