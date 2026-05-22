n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
l = a[0]
s = a[0]
for i in range(1, n):
    if a[i] > l:
        l = a[i]
    if a[i] < s:
        s = a[i]
print("Largest:", l)
print("Smallest:", s)
