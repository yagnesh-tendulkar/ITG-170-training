n=input("Enter n:")
l=len(n)
fou=0
f=int(n[0])
for i in range(1,l):
    if(int(n[i])!=f):
        fou=1
        print("Not Equal")
        break
if(fou==0):
    print("Equal")
