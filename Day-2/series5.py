#1/1+1/4+1/9+…1/N^2


n = int(input("enter n value:"))
 
sum = 0 

for i in range(1,n+1):
	sum += 1/(i*i)
print(i)
