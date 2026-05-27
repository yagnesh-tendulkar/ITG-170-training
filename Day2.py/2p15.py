n=input("Enter n:")
l=len(n)
sum=0
for i in range(0,l,2):
    sum+=int(n[i])
print(sum)
