rows=5

for i in range(0,rows):
    for j in range(0,rows):
        if i>=j:
            print(i-j+1, end=' ')
    print()