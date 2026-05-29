#sum of digits using recursion
def sum_digits(n):
    if n==0 :return 0
    return n%10 + sum_digits(n//10)
n = int(input("Enter a number: "))
result = sum_digits(n)
print(f"The sum of the digits of {n} is: {result}")