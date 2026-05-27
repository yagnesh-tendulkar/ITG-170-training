n=input("Enter n:")
esum=0
osum=0
l=len(n)
for i in range(0,l):
    if(i%2==0):
        esum+=int(n[i])
    else:
        osum+=int(n[i])
print("EvenSum:",esum)
print("OddSum:",osum)