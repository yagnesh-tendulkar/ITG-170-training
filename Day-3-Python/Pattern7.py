rows=5

for i in range(rows,-1,-1):
    for j in range(rows,0,-1):
        if i<j:
            print(j, end=' ')
    print()