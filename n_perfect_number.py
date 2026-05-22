n = int(input("Enter how many perfect numbers: "))

count = 0
num = 1

while count < n:

    divisor_sum = 0

    for i in range(1, num//2):

        if num % i == 0:
            divisor_sum += i

    if divisor_sum == num:
        print(num)
        count += 1

    num += 1