n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
for i in range(n):
    for j in range(i + 1, n):
        if a[i] < a[j]:
            t = a[i]
            a[i] = a[j]
            a[j] = t
for i in range(n):
    print(a[i])
