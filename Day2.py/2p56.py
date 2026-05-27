n = 7
for i in range(n, 0, -1):
    ch = 65
    for j in range(1, i + 1):
        print(chr(ch), end=" ")
        ch += 1
    print()