# 1/1! + 1/2! + 1/3! + ... + 1/n!

n = int(input("Enter the value of n: "))

sum_series = 0
factorial = 1

for i in range(1, n + 1):
    factorial *= i
    sum_series += 1 / factorial

print("Sum of the series is:", sum_series)
