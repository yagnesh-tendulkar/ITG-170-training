n = int(input("Enter the value of n: "))

count = 0
num = 1

print("First", n, "perfect numbers are:")

while count < n:
    sum_divisors = 0

    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i

    if sum_divisors == num:
        print(num)
        count += 1

    num += 1
