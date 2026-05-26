n=int(input("Enter the n value "))
for i in range(1,n+1):
    ch=65
    for j in range(i):
        print(chr(ch),end=" ")
        ch+=1
    print()