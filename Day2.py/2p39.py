n = int(input("Enter n: "))

s = 0
for i in range(n):
    s += 1 / (2 ** i)

print("Sum =", s)