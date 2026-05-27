n=int(input("Enter n:"))
for i in range(1,int(n/2)+2):
    for j in range(1,int(n/2)-i+2):
        print(" ",end="")
    for k in range(0,(2*i)-1):
        print("*",end="")
    print()
for i in range(1,n-(int(n/2)+1)+1):
    for j in range(1,i+1):
        print(" ",end="")
    for k in range((n-int(n/2))+(2-i),1,-2):
        print("*",end="")
    print()

