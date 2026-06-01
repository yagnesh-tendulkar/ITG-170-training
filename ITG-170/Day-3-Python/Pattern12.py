row=7

for i in range(1,row+1):
    for j in range(1,row+1):
        if i>j:
            print(j,end='*')
        elif i==j:
            print(j,end='')

    print()