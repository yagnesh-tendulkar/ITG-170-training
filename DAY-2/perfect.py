#perfect number : sum of divisors equals to the number
n = int(input("Enter a number: "))
divisors_sum = sum(i for i in range(1, n) if n % i == 0)
if divisors_sum == n:
    print(f"{n} is a Perfect Number")
else:
    print(f"{n} is NOT a Perfect Number")