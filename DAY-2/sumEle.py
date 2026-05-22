n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
s = 0
for i in range(n):
    s += a[i]
print(s)
