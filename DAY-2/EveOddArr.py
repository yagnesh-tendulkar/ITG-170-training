n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
print("Even numbers:")
for i in range(n):
    if a[i] % 2 == 0:
        print(a[i])
print("Odd numbers:")
for i in range(n):
    if a[i] % 2 != 0:
        print(a[i])
