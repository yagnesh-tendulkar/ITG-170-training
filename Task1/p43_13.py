n=int(input("Enter the n value "))
for i in range(1,n+1):
    for j in range(1,i):
        print(j,end="*")
    print(i)