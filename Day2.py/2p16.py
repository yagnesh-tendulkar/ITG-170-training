n=input("Enter n:")
dig=int(input("Enter a digit:"))
l=len(n)
count=0
for i in range(0,l):
    if(int(n[i])==dig):
        count+=1
print(count)
