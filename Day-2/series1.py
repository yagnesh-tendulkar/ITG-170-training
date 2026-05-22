# 1/1 + 1/2 + 1/3 + ... + 1/N

n = int(input("Enter the value of N: "))

sum_series = 0

for i in range(1, n + 1):
    sum_series += 1 / i

print("Sum of the series is:", sum_series)
