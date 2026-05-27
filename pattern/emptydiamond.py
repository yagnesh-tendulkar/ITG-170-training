rows=6
for i in range(rows):
    for j in range(rows-i,-1,-1):
        print(" ",end=" ")
    for j in range(1,2*i-1):
        print("*"*j,end=" ")
    print()