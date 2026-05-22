m = int(input())
n = int(input())

for i in range(m, n + 1):
    s = 0
    for j in range(1, i):
        if i % j == 0:
            s += j
    if s == i:
        print(i)
