# Checks whether a number is a Perfect Number without recursion

def check_perfect(number):
    sum_of_divisors = 0

    for i in range(1, number):
        if number % i == 0:
            sum_of_divisors += i

    if sum_of_divisors == number:
        print(number, "is a Perfect Number")
    else:
        print(number, "is not a Perfect Number")


input_number = int(input("Enter a number: "))
check_perfect(input_number)