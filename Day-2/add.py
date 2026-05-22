num = int(input("Enter a number: "))

last_digit = num % 10
first_digit = num

while first_digit >= 10:
    first_digit = first_digit // 10

sum_digits = first_digit + last_digit

print("Sum of first and last digit is:", sum_digits)
