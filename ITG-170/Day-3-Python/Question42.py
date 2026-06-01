def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

N = int(input("Enter N: "))
sum_series = 0.0

for i in range(1, N+1):
    sum_series += 1 / factorial(i)

print(f"Sum of the series is: {sum_series}")