m = int(input("Enter starting number: "))
n = int(input("Enter ending number: "))

for num in range(m, n + 1):
    sum = 0

    for i in range(1, num):
        if num % i == 0:
            sum += i

    if sum == num:
        print(num, end=" ")