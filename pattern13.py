row=int(input("enter number of rows ."))
ch=65
for i in range(row+1):
    for j in range(row-i):
        print(chr(ch+j),end=" ")
    print()      