rows=7
for i in range(0, rows+1):
    ascii = 65

    for j in range(rows,-1,-1):
        if j>i:
            print(chr(ascii), end=' ')
            ascii+=1
    print()