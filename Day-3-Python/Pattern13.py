rows=6

for i in range(0, rows+1):
    ascii = 65
    for j in range(0, rows+1):
        if i>j:
            print(chr(ascii), end=' ')
            ascii+=1
    print()