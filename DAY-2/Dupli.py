n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
for i in range(n):
    for j in range(i + 1, n):
        if a[i] == a[j]:
            print(a[i])
            break
