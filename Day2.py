# Program 1 : Positive or Negative Number

num = int(input("Enter number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Program 2 : Student Pass/Fail and Rank

marks = int(input("Enter marks: "))

if marks >= 35:
    print("Pass")
    
    if marks >= 90:
        print("Rank: A")
    elif marks >= 75:
        print("Rank: B")
    elif marks >= 60:
        print("Rank: C")
    else:
        print("Rank: D")
else:
    print("Fail")

# Program 3 : Uppercase, Lowercase, Digit, or Special Character

ch = input("Enter character: ")

if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")

# Program 4 : Biggest Among Two Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is biggest")
else:
    print(b, "is biggest")

# Program 5 : Square of Numbers up to 20

for i in range(1, 21):
    print(i, "=", i*i)

# Program 6 : Print n Even Numbers

n = int(input("Enter n: "))

for i in range(1, n+1):
    print(i*2)

# Program 7 : Sum of Even Numbers Between 1 to n

n = int(input("Enter n: "))
sum = 0

for i in range(2, n+1, 2):
    sum += i

print("Sum =", sum)

# Program 8 : Prime Numbers from 1 to 10

for num in range(2, 11):
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num)

# Program 9 : Square of Numbers up to 20

for i in range(1, 21):
    print(i*i)

# Program 10 : Factorial of n

n = int(input("Enter number: "))
fact = 1

for i in range(1, n+1):
    fact *= i

print("Factorial =", fact)

# Program 11 : Perfect Number

n = int(input("Enter number: "))
sum = 0

for i in range(1, n):
    if n % i == 0:
        sum += i

if sum == n:
    print("Perfect Number")
else:
    print("Not Perfect Number")

# Program 12 : Fibonacci Series

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

# Program 13 : Biggest Digit in a Number

n = int(input("Enter number: "))
big = 0

while n > 0:
    digit = n % 10

    if digit > big:
        big = digit

    n //= 10

print("Biggest digit =", big)

# Program 14  : Sum of Digits Using Recursion

def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

n = int(input("Enter number: "))
print(sum_digits(n))

# Program 15 :Sum of Alternative Digits

n = input("Enter number: ")

sum = 0

for i in range(0, len(n), 2):
    sum += int(n[i])

print("Sum =", sum)

# Program 16 : Occurrences of a Digit

n = input("Enter number: ")
digit = input("Enter digit to count: ")

count = n.count(digit)

print("Occurrences =", count)

# Program 17 : All Digits Equal or Not

n = input("Enter number: ")

if all(ch == n[0] for ch in n):
    print("All digits are equal")
else:
    print("Digits are not equal")

# Program 18 : Add First and Last Digit

n = input("Enter number: ")

sum = int(n[0]) + int(n[-1])

print("Sum =", sum)

# Program 19 : Add Even and Odd Digits

n = input("Enter number: ")

even_sum = 0
odd_sum = 0

for digit in n:
    digit = int(digit)

    if digit % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit

print("Even Sum =", even_sum)
print("Odd Sum =", odd_sum)

# Program 20 : Reverse a Number

n = int(input("Enter number: "))
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

print("Reverse =", rev)

# Program 21 : Prime Numbers Between m and n

m = int(input("Enter start: "))
n = int(input("Enter end: "))

for num in range(m, n+1):
    if num > 1:
        prime = True

        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        if prime:
            print(num)

# Program 22 : Print n Prime Numbers

n = int(input("Enter n: "))

count = 0
num = 2

while count < n:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num)
        count += 1

    num += 1

# Program 23 : Perfect Numbers Between m and n

m = int(input("Enter start: "))
n = int(input("Enter end: "))

for num in range(m, n+1):
    sum = 0

    for i in range(1, num):
        if num % i == 0:
            sum += i

    if sum == num:
        print(num)

# Program 24 : Print n Perfect Numbers

n = int(input("Enter n: "))

count = 0
num = 1

while count < n:
    sum = 0

    for i in range(1, num):
        if num % i == 0:
            sum += i

    if sum == num:
        print(num)
        count += 1

    num += 1

# Program 25 : Armstrong Numbers Between 1 and 1000

for num in range(1, 1001):
    temp = num
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    if sum == num:
        print(num)

# Program 26 : Sum of Natural Numbers

n = int(input("Enter n: "))

sum = n * (n + 1) // 2

print("Sum =", sum)

# Program 27: Copy Array Elements

arr1 = [1, 2, 3, 4]
arr2 = arr1.copy()

print(arr2)

# Program 28 : Frequency of Each Element

arr = [1, 2, 2, 3, 1, 4]

for i in arr:
    print(i, "=", arr.count(i))

# Program 29 : Duplicate Elements in Array

arr = [1, 2, 3, 2, 4, 1]

duplicates = []

for i in arr:
    if arr.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print(duplicates)

# Program 30 : Reverse Array

arr = [1, 2, 3, 4, 5]

print(arr[::-1])

# Program 31 : Largest and Smallest in Array

arr = [5, 2, 9, 1, 7]

print("Largest =", max(arr))
print("Smallest =", min(arr))

# Program 32 : Sort Array in Descending Order

arr = [5, 1, 4, 2]

arr.sort(reverse=True)

print(arr)

# Program 33 : Sum of Array Elements

arr = [1, 2, 3, 4]

print("Sum =", sum(arr))

# Program 34 : Odd and Even Numbers from Array

arr = [1, 2, 3, 4, 5, 6]

print("Even Numbers:")
for i in arr:
    if i % 2 == 0:
        print(i)

print("Odd Numbers:")
for i in arr:
    if i % 2 != 0:
        print(i)

# Program 35 : Happy Number

n = int(input("Enter number: "))

while n != 1 and n != 4:
    sum = 0

    while n > 0:
        digit = n % 10
        sum += digit * digit
        n //= 10

    n = sum

if n == 1:
    print("Happy Number")
else:
    print("Not Happy Number")

# Program 36 : Sum of Series 1 + 1/2 + 1/3 + ... + 1/N

n = int(input("Enter n: "))
sum = 0

for i in range(1, n+1):
    sum += 1/i

print(sum)

# Program 37 : Sum of Series 1 + 1/2² + 1/3² ...

n = int(input("Enter n: "))
sum = 0

for i in range(1, n+1):
    sum += 1/(i*i)

print(sum)

# Program 38 : Sum of Series

n = int(input("Enter n: "))
sum = 0

for i in range(1, n+1):
    sum += 1/(i**(i-1))

print(sum)

# Program 39 : Sum of Series 1/2⁰ + 1/2¹ ...

n = int(input("Enter n: "))
sum = 0

for i in range(n):
    sum += 1/(2**i)

print(sum)

# Program 40 : Sum of Series 1/1! + 1/2! ...

import math

n = int(input("Enter n: "))
sum = 0

for i in range(1, n+1):
    sum += 1/math.factorial(i)

print(sum)

# Program 41 : Sum of Series 1/1 + 1/4 + 1/9 ...

n = int(input("Enter n: "))
sum = 0

for i in range(1, n+1):
    sum += 1/(i*i)

print(sum)

# Program 42 : Sum of Series 1/1! + 1/2! ...

import math

n = int(input("Enter n: "))
sum = 0

for i in range(1, n+1):
    sum += 1/math.factorial(i)

print(sum)

# Program 43 : Pattern Programs 

rows = 5

for i in range(1, rows+1):
    for j in range(i):
        print("*", end=" ")
    print()

# Program 44 : Python Access Modifiers

class Student:
    public_var = "Public"

    def __init__(self):
        self._protected = "Protected"
        self.__private = "Private"

obj = Student()

print(obj.public_var)
print(obj._protected)

# Program 45: Package with Multiple Classes

# calculator/add.py

class Add:
    def sum(self, a, b):
        return a + b

# calculator/sub.py

class Sub:
    def minus(self, a, b):
        return a - b
    
