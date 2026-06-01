rows= 5
for i in range(rows):
    for j in range(rows-i-1,-1,-1):
        print(' ',end='')
    num=1
    for k in range(i*2+1):
        print(num,end='')
        if ((i*2+1)/2-1)>k:
            num+=1
        else:
            num-=1
    print()
for i in range(rows+1):
    for l in range(i):
        print('*',end='')
    print()