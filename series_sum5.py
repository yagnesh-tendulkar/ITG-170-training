n = int(input("Enter N: "))

total = 0

for i in range(1, n + 1):
    total += 1 / (i * i)

print("Sum =", total)