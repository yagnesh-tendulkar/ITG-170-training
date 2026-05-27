# Function to check whether a number is positive or negative
def check_positive_or_negative():
    number = int(input("Enter a number: "))
    if number > 0:
        print("Positive Number")
    elif number < 0:
        print("Negative Number")
    else:
        print("Zero")

# Function to check student pass/fail and rank
def check_student_result():
    marks = int(input("Enter student marks: "))
    if marks >= 35:
        print("Student Passed")
        if marks >= 90:
            print("Rank Obtained: A Grade")
        elif marks >= 75:
            print("Rank Obtained: B Grade")
        elif marks >= 60:
            print("Rank Obtained: C Grade")
        else:
            print("Rank Obtained: D Grade")
    else:
        print("Student Failed")

# Function to check character type
def check_character_type():
    character = input("Enter a character: ")
    if character.isupper():
        print("Uppercase Character")
    elif character.islower():
        print("Lowercase Character")
    elif character.isdigit():
        print("Digit")
    else:
        print("Special Character")

# Function to find biggest among two numbers
def find_biggest_between_two_numbers():
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    if first_number > second_number:
        print("Biggest Number:", first_number)
    else:
        print("Biggest Number:", second_number)

# Function to print squares up to 20
def print_squares_upto_20():
    for number in range(1, 21):
        print(number, "Square =", number * number)

# Function to print n even numbers
def print_n_even_numbers():
    limit = int(input("Enter value of n: "))
    for number in range(1, limit + 1):
        print(number * 2, end=" ")

# Function to find sum of even numbers
def sum_of_even_numbers():
    limit = int(input("Enter value of n: "))
    total_sum = 0
    for number in range(2, limit + 1, 2):
        total_sum += number
    print("Sum of Even Numbers:", total_sum)

# Function to print prime numbers from 1 to 10
def print_prime_numbers_1_to_10():
    for number in range(2, 11):
        is_prime = True
        for divisor in range(2, number):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            print(number)

# Function to calculate factorial
def calculate_factorial():
    number = int(input("Enter a number: "))
    factorial = 1
    for value in range(1, number + 1):
        factorial *= value
    print("Factorial =", factorial)

# Function to check perfect number
def check_perfect_number():
    number = int(input("Enter a number: "))
    divisor_sum = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            divisor_sum += divisor
    if divisor_sum == number:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")

# Function to print Fibonacci series
def print_fibonacci_series():
    limit = int(input("Enter number of terms: "))
    first_number = 0
    second_number = 1
    for count in range(limit):
        print(first_number, end=" ")
        next_number = first_number + second_number
        first_number = second_number
        second_number = next_number

# Function to find biggest digit in a number
def find_biggest_digit():
    number = int(input("Enter a number: "))
    biggest_digit = 0
    while number > 0:
        digit = number % 10
        if digit > biggest_digit:
            biggest_digit = digit
        number //= 10
    print("Biggest Digit =", biggest_digit)

# Function to find sum of digits using recursion
def sum_of_digits_using_recursion(number):
    if number == 0:
        return 0
    return number % 10 + sum_of_digits_using_recursion(number // 10)

# Function to find alternative digit sum
def alternative_digit_sum():
    number = input("Enter a number: ")
    total_sum = 0
    for index in range(0, len(number), 2):
        total_sum += int(number[index])
    print("Alternative Digit Sum =", total_sum)

# Function to count occurrences of a digit
def count_digit_occurrences():
    number = input("Enter a number: ")
    digit = input("Enter digit to count: ")
    occurrence_count = 0
    for value in number:
        if value == digit:
            occurrence_count += 1
    print("Number of Occurrences =", occurrence_count)

# Function to check whether all digits are equal
def check_all_digits_equal():
    number = input("Enter a number: ")
    all_equal = True
    for digit in number:
        if digit != number[0]:
            all_equal = False
            break
    if all_equal:
        print("All Digits are Equal")
    else:
        print("Digits are Not Equal")

# Function to add first and last digit
def add_first_and_last_digit():
    number = input("Enter a number: ")
    first_digit = int(number[0])
    last_digit = int(number[-1])
    print("Sum =", first_digit + last_digit)

# Function to add even and odd digits
def add_even_and_odd_digits():
    number = input("Enter a number: ")
    even_digit_sum = 0
    odd_digit_sum = 0
    for digit in number:
        digit = int(digit)
        if digit % 2 == 0:
            even_digit_sum += digit
        else:
            odd_digit_sum += digit
    print("Even Digit Sum =", even_digit_sum)
    print("Odd Digit Sum =", odd_digit_sum)

# Function to reverse a number
def reverse_a_number():
    number = int(input("Enter a number: "))
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10
    print("Reversed Number =", reversed_number)

# Function to print prime numbers between m and n
def print_prime_numbers_between_m_and_n():
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))
    for number in range(start, end + 1):
        if number > 1:
            is_prime = True
            for divisor in range(2, number):
                if number % divisor == 0:
                    is_prime = False
                    break
            if is_prime:
                print(number)

# Function to print n prime numbers
def print_n_prime_numbers():
    limit = int(input("Enter value of n: "))
    count = 0
    number = 2
    while count < limit:
        is_prime = True
        for divisor in range(2, number):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            print(number, end=" ")
            count += 1
        number += 1

# Function to print perfect numbers between m and n
def print_perfect_numbers_between_m_and_n():
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))
    for number in range(start, end + 1):
        divisor_sum = 0
        for divisor in range(1, number):
            if number % divisor == 0:
                divisor_sum += divisor
        if divisor_sum == number:
            print(number)

# Function to print n perfect numbers
def print_n_perfect_numbers():
    limit = int(input("Enter how many perfect numbers: "))
    count = 0
    number = 1
    while count < limit:
        divisor_sum = 0
        for divisor in range(1, number):
            if number % divisor == 0:
                divisor_sum += divisor
        if divisor_sum == number:
            print(number, end=" ")
            count += 1
        number += 1

# Function to print Armstrong numbers from 1 to 1000
def print_armstrong_numbers():
    for number in range(1, 1001):
        temporary_number = number
        digit_sum = 0
        digit_count = len(str(number))
        while temporary_number > 0:
            digit = temporary_number % 10
            digit_sum += digit ** digit_count
            temporary_number //= 10
        if digit_sum == number:
            print(number)

# Function to find sum of natural numbers
def sum_of_natural_numbers():
    limit = int(input("Enter value of n: "))
    total_sum = 0
    for number in range(1, limit + 1):
        total_sum += number
    print("Sum of Natural Numbers =", total_sum)

# ---------------- MAIN MENU ---------------- #

print("\n--------- PYTHON ASSIGNMENT PROGRAMS ---------\n")
print("1. Check Positive or Negative")
print("2. Student Pass or Fail")
print("3. Check Character Type")
print("4. Biggest Among Two Numbers")
print("5. Print Squares up to 20")
print("6. Print n Even Numbers")
print("7. Sum of Even Numbers")
print("8. Prime Numbers from 1 to 10")
print("9. Factorial of a Number")
print("10. Perfect Number")
print("11. Fibonacci Series")
print("12. Biggest Digit in a Number")
print("13. Sum of Digits Using Recursion")
print("14. Sum of Alternative Digits")
print("15. Count Digit Occurrences")
print("16. Check All Digits Equal")
print("17. Add First and Last Digit")
print("18. Add Even and Odd Digits")
print("19. Reverse a Number")
print("20. Prime Numbers Between m and n")
print("21. Print n Prime Numbers")
print("22. Perfect Numbers Between m and n")
print("23. Print n Perfect Numbers")
print("24. Armstrong Numbers from 1 to 1000")
print("25. Sum of Natural Numbers")

choice = int(input("\nEnter your choice: "))

if choice == 1:
    check_positive_or_negative()
elif choice == 2:
    check_student_result()
elif choice == 3:
    check_character_type()
elif choice == 4:
    find_biggest_between_two_numbers()
elif choice == 5:
    print_squares_upto_20()
elif choice == 6:
    print_n_even_numbers()
elif choice == 7:
    sum_of_even_numbers()
elif choice == 8:
    print_prime_numbers_1_to_10()
elif choice == 9:
    calculate_factorial()
elif choice == 10:
    check_perfect_number()
elif choice == 11:
    print_fibonacci_series()
elif choice == 12:
    find_biggest_digit()
elif choice == 13:
    number = int(input("Enter a number: "))
    print("Sum of Digits =", sum_of_digits_using_recursion(number))
elif choice == 14:
    alternative_digit_sum()
elif choice == 15:
    count_digit_occurrences()
elif choice == 16:
    check_all_digits_equal()
elif choice == 17:
    add_first_and_last_digit()
elif choice == 18:
    add_even_and_odd_digits()
elif choice == 19:
    reverse_a_number()
elif choice == 20:
    print_prime_numbers_between_m_and_n()
elif choice == 21:
    print_n_prime_numbers()
elif choice == 22:
    print_perfect_numbers_between_m_and_n()
elif choice == 23:
    print_n_perfect_numbers()
elif choice == 24:
    print_armstrong_numbers()
elif choice == 25:
    sum_of_natural_numbers()
else:
    print("Invalid Choice")