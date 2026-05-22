num = int(input("Enter a number: "))

temp = num
last_digit = temp % 10
all_equal = True

while temp > 0:
    digit = temp % 10

    if digit != last_digit:
        all_equal = False
        break

    temp = temp // 10

if all_equal:
    print("All digits are equal")
else:
    print("All digits are not equal")
