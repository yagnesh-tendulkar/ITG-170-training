#Program to Print Armstrong Number between 1 to 1000.
for num in range(1, 1001):

    temp = num
    sum = 0

    while temp > 0:
        rem = temp % 10
        sum = sum + (rem ** 3)
        temp = temp // 10

    if sum == num:
        print(num)