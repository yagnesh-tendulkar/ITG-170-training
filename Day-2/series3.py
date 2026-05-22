# 1/1^0+1/2^1+1/3^2+1/4^3+1/5^4.
n = int(input("Enter the value of n: "))

sum_series = 0

for i in range(1, n + 1):
    sum_series += 1 / (i ** (i - 1))

print("Sum of the series is:", sum_series)
