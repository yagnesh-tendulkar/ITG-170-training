n=5
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    for k in range(i,1,-1):
        print(k-1,end=" ")
    print()
k_n =n-1
for i in range(1,k_n+1):
    for p in range(1,i+1):
        print(" ",end = " ")
    for k in range(1,k_n -i +2):
        print(k,end=" ")
    for y in range(k_n-i,0,-1):
        print(y,end=" ")
    print()    