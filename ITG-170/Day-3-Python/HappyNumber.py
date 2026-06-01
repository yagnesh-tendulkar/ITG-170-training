def is_happy(n):
    seen = []

    while n != 1:
        sum_sq = 0
        temp = n
        while temp > 0:
            digit = temp % 10
            sum_sq += digit * digit
            temp //= 10

        if sum_sq in seen:
            return False
        seen.append(sum_sq)
        n = sum_sq

    return True


num = int(input("Enter a number: "))
if is_happy(num):
    print(f"{num} is a Happy Number")
else:
    print(f"{num} is not a Happy Number")