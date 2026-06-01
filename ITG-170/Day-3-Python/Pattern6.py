rows=5
num=0
for i in range(0,rows):
    for j in range(0,rows):
        if i>=j:
            print(num + 1, end=' ')
            num+=1
    print()