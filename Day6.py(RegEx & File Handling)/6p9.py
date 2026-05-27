def perfect(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    if total == n:
        return "Perfect Number"
    else:
        return "Not Perfect Number"
print(perfect(28))