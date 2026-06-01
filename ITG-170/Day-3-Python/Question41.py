N = int(input("Enter N: "))
sum_series = 0.0

for i in range(1, N+1):
    sum_series += 1 / (i**2)

print(f"Sum of the series is: {sum_series}")