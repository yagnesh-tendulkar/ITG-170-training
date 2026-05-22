num = int(input("Enter a number: "))

happy = num

while num != 1 and num != 4:
    sum_digits = 0

    while num > 0:
        digit = num % 10
        sum_digits += digit * digit
        num = num // 10

    num = sum_digits

if num == 1:
    print(happy, "is a Happy Number")
else:
    print(happy, "is not a Happy Number")
