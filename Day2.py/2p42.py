n = int(input("Enter n:"))
s = 0
fact = 1
for i in range(1, n + 1):
    fact *= i
    s += 1 / fact
print("Sum =", s)