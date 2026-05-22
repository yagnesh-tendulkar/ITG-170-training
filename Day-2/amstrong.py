print("Armstrong numbers between 1 and 1000 are:")

for num in range(1, 1001):
    temp = num
    sum_digits = 0

    while temp > 0:
        digit = temp % 10
        sum_digits += digit ** 3
        temp = temp // 10

    if sum_digits == num:
        print(num)
