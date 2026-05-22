# 1/1 + 1/2² + 1/3² + 1/4² + ... + 1/n²

n = int(input("Enter the value of n: "))

total= 0

for i in range(1, n + 1):
    sum_series += 1 / (i * i)



for i in range(1,n+1):
	total += 1/ (i*i)
print("Sum of the series is:", sum_series)


