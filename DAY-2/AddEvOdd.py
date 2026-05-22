n = int(input())
even = 0
odd = 0

while n > 0:
    d = n % 10
    if d % 2 == 0:
        even += d
    else:
        odd += d
    n //= 10

print("Even Sum =", even)
print("Odd Sum =", odd)
