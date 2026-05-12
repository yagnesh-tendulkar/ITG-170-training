n=5
for i in range(1,n+1):
    for j in range(1,i):
        print(" ", end="")
    for k in range(i,n+1):
        print(k, end =" ")
    print()
for i in range(2,n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(n-i+1,n+1):
        print(k, end =" ")
    print()