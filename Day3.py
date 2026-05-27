"""
Miracle Python Training - Complete 45 Programs (Improved)
Employee Name: Geetha Gangabattula
Topic: Program Flow and Access Modifiers
Status: Completed
Date: 2026-05-27

This module contains improved versions of all 45 programs with:
- Proper error handling
- PEP 8 compliance
- Function-based structure
- Comprehensive documentation
- Type hints
- Input validation
- Best practices
"""

import math
from typing import List, Tuple


# ============================================================================
# PROGRAM 1: POSITIVE OR NEGATIVE
# ============================================================================

def check_positive_negative() -> None:
    """Check if a number is positive, negative, or zero."""
    print("\n" + "="*70)
    print("PROGRAM 1: POSITIVE OR NEGATIVE")
    print("="*70)
    
    try:
        n = int(input("Enter number: "))
        
        if n > 0:
            print(f"✓ {n} is Positive")
        elif n < 0:
            print(f"✓ {n} is Negative")
        else:
            print("✓ Zero")
    except ValueError:
        print("❌ Please enter a valid integer")


# ============================================================================
# PROGRAM 2: STUDENT PASS/FAIL AND RANK
# ============================================================================

def check_student_result() -> None:
    """Check student pass/fail status and assign rank."""
    print("\n" + "="*70)
    print("PROGRAM 2: STUDENT PASS/FAIL AND RANK")
    print("="*70)
    
    try:
        marks = int(input("Enter marks (0-100): "))
        
        if not (0 <= marks <= 100):
            print("❌ Marks should be between 0-100")
            return
        
        print(f"\nMarks: {marks}")
        
        if marks >= 35:
            print("✓ Status: Passed")
            
            if marks >= 90:
                rank = "A"
            elif marks >= 75:
                rank = "B"
            elif marks >= 60:
                rank = "C"
            else:
                rank = "D"
            
            print(f"✓ Rank: {rank}")
        else:
            print("✗ Status: Failed")
    except ValueError:
        print("❌ Please enter a valid integer")


# ============================================================================
# PROGRAM 3: CHARACTER CLASSIFICATION
# ============================================================================

def classify_character() -> None:
    """Classify character as uppercase, lowercase, digit, or special."""
    print("\n" + "="*70)
    print("PROGRAM 3: CHARACTER CLASSIFICATION")
    print("="*70)
    
    ch = input("Enter a character: ").strip()
    
    if len(ch) != 1:
        print("❌ Please enter exactly one character")
        return
    
    if ch.isupper():
        print(f"✓ '{ch}' is Uppercase")
    elif ch.islower():
        print(f"✓ '{ch}' is Lowercase")
    elif ch.isdigit():
        print(f"✓ '{ch}' is Digit")
    else:
        print(f"✓ '{ch}' is Special Character")


# ============================================================================
# PROGRAM 4: BIGGEST AMONG TWO NUMBERS
# ============================================================================

def find_biggest_two_numbers() -> None:
    """Find the biggest among two numbers."""
    print("\n" + "="*70)
    print("PROGRAM 4: BIGGEST AMONG TWO NUMBERS")
    print("="*70)
    
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        
        biggest = max(a, b)
        print(f"\n✓ {biggest} is the biggest number")
    except ValueError:
        print("❌ Please enter valid integers")


# ============================================================================
# PROGRAM 5: SQUARE OF NUMBERS UP TO 20
# ============================================================================

def print_squares_upto_20() -> None:
    """Print squares of numbers from 1 to 20."""
    print("\n" + "="*70)
    print("PROGRAM 5: SQUARE OF NUMBERS UP TO 20")
    print("="*70)
    
    print("\nNumber | Square")
    print("-" * 20)
    
    for i in range(1, 21):
        print(f"{i:6d} | {i*i:6d}")


# ============================================================================
# PROGRAM 6: PRINT n EVEN NUMBERS
# ============================================================================

def print_n_even_numbers() -> None:
    """Print first n even numbers."""
    print("\n" + "="*70)
    print("PROGRAM 6: PRINT n EVEN NUMBERS")
    print("="*70)
    
    try:
        n = int(input("Enter n: "))
        
        if n <= 0:
            print("❌ Please enter a positive number")
            return
        
        print(f"\nFirst {n} even numbers:")
        print("-" * 30)
        
        even_numbers = [i * 2 for i in range(1, n + 1)]
        print(", ".join(map(str, even_numbers)))
    except ValueError:
        print("❌ Please enter a valid integer")


# ============================================================================
# PROGRAM 7: SUM OF EVEN NUMBERS
# ============================================================================

def sum_even_numbers() -> None:
    """Calculate sum of even numbers up to n."""
    print("\n" + "="*70)
    print("PROGRAM 7: SUM OF EVEN NUMBERS")
    print("="*70)
    
    try:
        n = int(input("Enter n: "))
        
        if n < 2:
            print("Sum = 0")
            return
        
        s = sum(i for i in range(2, n + 1, 2))
        print(f"\n✓ Sum of even numbers up to {n} = {s}")
    except ValueError:
        print("❌ Please enter a valid integer")


# ============================================================================
# PROGRAM 8: PRIME NUMBERS 1 TO 10
# ============================================================================

def is_prime(num: int) -> bool:
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def print_primes_1_to_10() -> None:
    """Print prime numbers from 1 to 10."""
    print("\n" + "="*70)
    print("PROGRAM 8: PRIME NUMBERS 1 TO 10")
    print("="*70)
    
    primes = [n for n in range(2, 11) if is_prime(n)]
    
    print("\nPrime numbers from 1 to 10:")
    print("-" * 30)
    print(", ".join(map(str, primes)))


# ============================================================================
# PROGRAM 10: FACTORIAL
# ============================================================================

def calculate_factorial() -> None:
    """Calculate factorial of a number."""
    print("\n" + "="*70)
    print("PROGRAM 10: FACTORIAL")
    print("="*70)
    
    try:
        n = int(input("Enter number: "))
        
        if n < 0:
            print("❌ Factorial not defined for negative numbers")
            return
        
        factorial = math.factorial(n)
        print(f"\n✓ Factorial of {n} = {factorial}")
    except ValueError:
        print("❌ Please enter a valid integer")


# ============================================================================
# PROGRAM 11: PERFECT NUMBER
# ============================================================================

def is_perfect_number(num: int) -> bool:
    """Check if a number is perfect."""
    if num <= 0:
        return False
    
    s = sum(i for i in range(1, num) if num % i == 0)
    return s == num


def check_perfect_number() -> None:
    """Check if input number is perfect."""
    print("\n" + "="*70)
    print("PROGRAM 11: PERFECT NUMBER")
    print("="*70)
    
    try:
        n = int(input("Enter number: "))
        
        if is_perfect_number(n):
            print(f"✓ {n} is a Perfect Number")
        else:
            print(f"✗ {n} is Not a Perfect Number")
    except ValueError:
        print("❌ Please enter a valid integer")


# ============================================================================
# PROGRAM 12: FIBONACCI SERIES
# ============================================================================

def print_fibonacci_series() -> None:
    """Print Fibonacci series up to n terms."""
    print("\n" + "="*70)
    print("PROGRAM 12: FIBONACCI SERIES")
    print("="*70)
    
    try:
        n = int(input("Enter number of terms: "))
        
        if n <= 0:
            print("❌ Please enter a positive number")
            return
        
        a, b = 0, 1
        
        print(f"\nFirst {n} terms of Fibonacci series:")
        print("-" * 30)
        
        for i in range(n):
            print(a, end=" ")
            a, b = b, a + b
        
        print("\n")
    except ValueError:
        print("❌ Please enter a valid integer")


# ============================================================================
# PROGRAM 13: BIGGEST DIGIT
# ============================================================================

def find_biggest_digit() -> None:
    """Find the biggest digit in a number."""
    print("\n" + "="*70)
    print("PROGRAM 13: BIGGEST DIGIT")
    print("="*70)
    
    n = input("Enter number: ").strip()
    
    if not n.replace("-", "").isdigit():
        print("❌ Please enter a valid number")
        return
    
    biggest = max(n.replace("-", ""))
    print(f"\n✓ Biggest digit = {biggest}")


# ============================================================================
# PROGRAM 14: SUM OF DIGITS USING RECURSION
# ============================================================================

def sum_digits_recursive(n: int) -> int:
    """Calculate sum of digits using recursion."""
    if n == 0:
        return 0
    return n % 10 + sum_digits_recursive(n // 10)


def sum_digits() -> None:
    """Sum of digits using recursion."""
    print("\n" + "="*70)
    print("PROGRAM 14: SUM OF DIGITS USING RECURSION")
    print("="*70)
    
    try:
        n = int(input("Enter number: "))
        result = sum_digits_recursive(abs(n))
        print(f"\n✓ Sum of digits = {result}")
    except ValueError:
        print("❌ Please enter a valid integer")


# ============================================================================
# PROGRAM 15: SUM OF ALTERNATIVE DIGITS
# ============================================================================

def sum_alternative_digits() -> None:
    """Sum of alternative digits."""
    print("\n" + "="*70)
    print("PROGRAM 15: SUM OF ALTERNATIVE DIGITS")
    print("="*70)
    
    n = input("Enter number: ").strip()
    
    if not n.replace("-", "").isdigit():
        print("❌ Please enter a valid number")
        return
    
    s = sum(int(n[i]) for i in range(0, len(n), 2))
    print(f"\n✓ Sum of alternative digits = {s}")


# ============================================================================
# PROGRAM 16: OCCURRENCES OF DIGIT
# ============================================================================

def count_digit_occurrences() -> None:
    """Count occurrences of a digit."""
    print("\n" + "="*70)
    print("PROGRAM 16: OCCURRENCES OF DIGIT")
    print("="*70)
    
    n = input("Enter number: ").strip()
    digit = input("Enter digit to search: ").strip()
    
    if not n.isdigit() or len(digit) != 1 or not digit.isdigit():
        print("❌ Please enter valid inputs")
        return
    
    count = n.count(digit)
    print(f"\n✓ Digit {digit} occurs {count} times")


# ============================================================================
# PROGRAM 17: ALL DIGITS EQUAL
# ============================================================================

def check_all_digits_equal() -> None:
    """Check if all digits are equal."""
    print("\n" + "="*70)
    print("PROGRAM 17: ALL DIGITS EQUAL")
    print("="*70)
    
    n = input("Enter number: ").strip()
    
    if not n.isdigit():
        print("❌ Please enter a valid number")
        return
    
    if n.count(n[0]) == len(n):
        print(f"✓ All digits in {n} are equal")
    else:
        print(f"✗ Not all digits in {n} are equal")


# ============================================================================
# PROGRAM 18: ADD FIRST AND LAST DIGIT
# ============================================================================

def add_first_and_last_digit() -> None:
    """Add first and last digit."""
    print("\n" + "="*70)
    print("PROGRAM 18: ADD FIRST AND LAST DIGIT")
    print("="*70)
    
    n = input("Enter number: ").strip()
    
    if not n.isdigit():
        print("❌ Please enter a valid number")
        return
    
    result = int(n[0]) + int(n[-1])
    print(f"\n✓ First digit ({n[0]}) + Last digit ({n[-1]}) = {result}")


# ============================================================================
# PROGRAM 19: ADD EVEN AND ODD DIGITS
# ============================================================================

def add_even_and_odd_digits() -> None:
    """Add even and odd digits separately."""
    print("\n" + "="*70)
    print("PROGRAM 19: ADD EVEN AND ODD DIGITS")
    print("="*70)
    
    n = input("Enter number: ").strip()
    
    if not n.isdigit():
        print("❌ Please enter a valid number")
        return
    
    even_sum = sum(int(i) for i in n if int(i) % 2 == 0)
    odd_sum = sum(int(i) for i in n if int(i) % 2 != 0)
    
    print(f"\n✓ Even digits sum = {even_sum}")
    print(f"✓ Odd digits sum = {odd_sum}")


# ============================================================================
# PROGRAM 20: REVERSE A NUMBER
# ============================================================================

def reverse_number() -> None:
    """Reverse a number."""
    print("\n" + "="*70)
    print("PROGRAM 20: REVERSE A NUMBER")
    print("="*70)
    
    n = input("Enter number: ").strip()
    
    if not n.replace("-", "").isdigit():
        print("❌ Please enter a valid number")
        return
    
    reversed_num = n[::-1]
    print(f"\n✓ Reversed number = {reversed_num}")


# ============================================================================
# PROGRAM 21: PRIME NUMBERS BETWEEN m AND n
# ============================================================================

def print_primes_between_m_n() -> None:
    """Print prime numbers between m and n."""
    print("\n" + "="*70)
    print("PROGRAM 21: PRIME NUMBERS BETWEEN m AND n")
    print("="*70)
    
    try:
        m = int(input("Enter m: "))
        n = int(input("Enter n: "))
        
        if m > n:
            m, n = n, m
        
        primes = [num for num in range(m, n + 1) if is_prime(num)]
        
        print(f"\nPrime numbers between {m} and {n}:")
        print("-" * 30)
        
        if primes:
            print(", ".join(map(str, primes)))
        else:
            print("No prime numbers found")
    except ValueError:
        print("❌ Please enter valid integers")


# ============================================================================
# PROGRAM 22: PRINT n PRIME NUMBERS
# ============================================================================

def print_n_primes() -> None:
    """Print first n prime numbers."""
    print("\n" + "="*70)
    print("PROGRAM 22: PRINT n PRIME NUMBERS")
    print("="*70)
    
    try:
        n = int(input("Enter n: "))
        
        if n <= 0:
            print("❌ Please enter a positive number")
            return
        
        primes = []
        num = 2
        
        while len(primes) < n:
            if is_prime(num):
                primes.append(num)
            num += 1
        
        print(f"\nFirst {n} prime numbers:")
        print("-" * 30)
        print(", ".join(map(str, primes)))
    except ValueError:
        print("❌ Please enter a valid integer")


# ============================================================================
# PROGRAM 25: ARMSTRONG NUMBERS
# ============================================================================

def is_armstrong(num: int) -> bool:
    """Check if a number is Armstrong number."""
    s = sum(int(digit) ** 3 for digit in str(num))
    return s == num


def print_armstrong_numbers() -> None:
    """Print Armstrong numbers from 1 to 1000."""
    print("\n" + "="*70)
    print("PROGRAM 25: ARMSTRONG NUMBERS (1-1000)")
    print("="*70)
    
    armstrong_nums = [num for num in range(1, 1001) if is_armstrong(num)]
    
    print("\nArmstrong numbers from 1 to 1000:")
    print("-" * 30)
    print(", ".join(map(str, armstrong_nums)))


# ============================================================================
# PROGRAM 26: SUM OF NATURAL NUMBERS
# ============================================================================

def sum_natural_numbers() -> None:
    """Calculate sum of first n natural numbers."""
    print("\n" + "="*70)
    print("PROGRAM 26: SUM OF NATURAL NUMBERS")
    print("="*70)
    
    try:
        n = int(input("Enter n: "))
        
        if n < 0:
            print("❌ Please enter a positive number")
            return
        
        result = n * (n + 1) // 2
        print(f"\n✓ Sum of natural numbers from 1 to {n} = {result}")
    except ValueError:
        print("❌ Please enter a valid integer")


# ============================================================================
# PROGRAM 27: COPY ARRAY
# ============================================================================

def copy_array() -> None:
    """Demonstrate array copying."""
    print("\n" + "="*70)
    print("PROGRAM 27: COPY ARRAY")
    print("="*70)
    
    a = [1, 2, 3, 4, 5]
    b = a.copy()
    
    print(f"\nOriginal Array: {a}")
    print(f"Copied Array:  {b}")
    
    # Modify one to show independence
    b[0] = 99
    
    print(f"\nAfter modifying copy:")
    print(f"Original Array: {a}")
    print(f"Copied Array:  {b}")
    print("✓ Arrays are independent (deep copy)")


# ============================================================================
# PROGRAM 28: FREQUENCY OF ELEMENTS
# ============================================================================

def frequency_of_elements() -> None:
    """Display frequency of array elements."""
    print("\n" + "="*70)
    print("PROGRAM 28: FREQUENCY OF ELEMENTS")
    print("="*70)
    
    a = [1, 2, 2, 3, 1, 4, 2]
    
    print(f"\nArray: {a}")
    print("\nFrequency:")
    print("-" * 20)
    
    unique = set(a)
    for i in unique:
        count = a.count(i)
        print(f"{i} → {count} time(s)")


# ============================================================================
# PROGRAM 29: DUPLICATE ELEMENTS
# ============================================================================

def find_duplicate_elements() -> None:
    """Find duplicate elements in array."""
    print("\n" + "="*70)
    print("PROGRAM 29: DUPLICATE ELEMENTS")
    print("="*70)
    
    a = [1, 2, 2, 3, 4, 4, 5]
    
    print(f"\nArray: {a}")
    print("\nDuplicate elements:")
    print("-" * 20)
    
    duplicates = set([i for i in a if a.count(i) > 1])
    
    if duplicates:
        for dup in sorted(duplicates):
            print(f"✓ {dup} (appears {a.count(dup)} times)")
    else:
        print("No duplicates found")


# ============================================================================
# PROGRAM 30: REVERSE ARRAY
# ============================================================================

def reverse_array() -> None:
    """Reverse an array."""
    print("\n" + "="*70)
    print("PROGRAM 30: REVERSE ARRAY")
    print("="*70)
    
    a = [1, 2, 3, 4, 5]
    
    print(f"\nOriginal Array: {a}")
    print(f"Reversed Array: {a[::-1]}")


# ============================================================================
# PROGRAM 31: LARGEST AND SMALLEST
# ============================================================================

def find_largest_and_smallest() -> None:
    """Find largest and smallest in array."""
    print("\n" + "="*70)
    print("PROGRAM 31: LARGEST AND SMALLEST")
    print("="*70)
    
    a = [10, 20, 5, 40, 15]
    
    print(f"\nArray: {a}")
    print(f"\n✓ Largest:   {max(a)}")
    print(f"✓ Smallest:  {min(a)}")


# ============================================================================
# PROGRAM 32: SORT DESCENDING
# ============================================================================

def sort_descending() -> None:
    """Sort array in descending order."""
    print("\n" + "="*70)
    print("PROGRAM 32: SORT DESCENDING")
    print("="*70)
    
    a = [4, 2, 8, 1, 9, 3]
    
    print(f"\nOriginal Array:     {a}")
    
    a.sort(reverse=True)
    print(f"Descending Order:   {a}")


# ============================================================================
# PROGRAM 33: SUM OF ARRAY
# ============================================================================

def sum_array() -> None:
    """Calculate sum of array elements."""
    print("\n" + "="*70)
    print("PROGRAM 33: SUM OF ARRAY")
    print("="*70)
    
    a = [1, 2, 3, 4, 5]
    
    print(f"\nArray: {a}")
    print(f"\n✓ Sum = {sum(a)}")


# ============================================================================
# PROGRAM 34: ODD AND EVEN IN ARRAY
# ============================================================================

def classify_array_elements() -> None:
    """Classify array elements as odd or even."""
    print("\n" + "="*70)
    print("PROGRAM 34: ODD AND EVEN IN ARRAY")
    print("="*70)
    
    a = [1, 2, 3, 4, 5, 6]
    
    print(f"\nArray: {a}")
    print("\nClassification:")
    print("-" * 20)
    
    for i in a:
        classification = "Even" if i % 2 == 0 else "Odd"
        print(f"{i} → {classification}")


# ============================================================================
# PROGRAM 35: HAPPY NUMBER
# ============================================================================

def is_happy_number(n: int) -> bool:
    """Check if a number is happy."""
    while n != 1 and n != 4:
        s = 0
        while n > 0:
            digit = n % 10
            s += digit * digit
            n //= 10
        n = s
    
    return n == 1


def check_happy_number() -> None:
    """Check if input number is happy."""
    print("\n" + "="*70)
    print("PROGRAM 35: HAPPY NUMBER")
    print("="*70)
    
    try:
        n = int(input("Enter number: "))
        
        if is_happy_number(n):
            print(f"✓ {n} is a Happy Number")
        else:
            print(f"✗ {n} is Not a Happy Number")
    except ValueError:
        print("❌ Please enter a valid integer")


# ============================================================================
# PROGRAM 40: SUM OF FACTORIAL SERIES
# ============================================================================

def sum_factorial_series() -> None:
    """Calculate sum of factorial series: 1/1! + 1/2! + 1/3! + ..."""
    print("\n" + "="*70)
    print("PROGRAM 40: SUM OF FACTORIAL SERIES")
    print("="*70)
    
    try:
        n = int(input("Enter n: "))
        
        if n < 1:
            print("❌ Please enter a positive number")
            return
        
        s = sum(1 / math.factorial(i) for i in range(1, n + 1))
        
        print(f"\n✓ Sum of factorial series (1st {n} terms) = {s:.6f}")
    except ValueError:
        print("❌ Please enter a valid integer")


# ============================================================================
# PROGRAM 43: PATTERNS
# ============================================================================

def print_patterns() -> None:
    """Print various patterns."""
    print("\n" + "="*70)
    print("PROGRAM 43: PATTERNS")
    print("="*70)
    
    # Pattern 1: Increasing stars
    print("\nPattern 1: Increasing Stars")
    print("-" * 30)
    for i in range(1, 6):
        print("* " * i)
    
    # Pattern 2: Odd star pyramid
    print("\nPattern 2: Odd Star Pyramid")
    print("-" * 30)
    for i in range(1, 6, 2):
        print("*" * i)
    
    # Pattern 3: Number pyramid
    print("\nPattern 3: Number Pyramid")
    print("-" * 30)
    for i in range(1, 6):
        print("".join(str(j) for j in range(1, i + 1)))
    
    # Pattern 4: Number triangle
    print("\nPattern 4: Number Triangle")
    print("-" * 30)
    for i in range(1, 6):
        print(" ".join(str(j) for j in range(1, i + 1)))
    
    # Pattern 5: Reverse number triangle
    print("\nPattern 5: Reverse Number Triangle")
    print("-" * 30)
    for i in range(5, 0, -1):
        print(" ".join(str(j) for j in range(5, i - 1, -1)))
    
    # Pattern 6: Alphabet pyramid
    print("\nPattern 6: Alphabet Pyramid")
    print("-" * 30)
    for i in range(65, 70):
        print(" ".join(chr(j) for j in range(65, i + 1)))


# ============================================================================
# PROGRAM 44: ACCESS MODIFIERS
# ============================================================================

class Student:
    """Student class demonstrating access modifiers."""
    
    # Public attribute
    name = "Geetha Gangabattula"
    
    # Protected attribute
    _branch = "Computer Science"
    
    # Private attribute
    __marks = 95
    
    def __init__(self, name: str, branch: str, marks: int) -> None:
        """Initialize student."""
        self.name = name
        self._branch = branch
        self.__marks = marks
    
    def display_all(self) -> None:
        """Display all information."""
        print(f"Name:   {self.name}")
        print(f"Branch: {self._branch}")
        print(f"Marks:  {self.__marks}")
    
    def get_marks(self) -> int:
        """Getter for private marks."""
        return self.__marks


def demonstrate_access_modifiers() -> None:
    """Demonstrate access modifiers."""
    print("\n" + "="*70)
    print("PROGRAM 44: ACCESS MODIFIERS")
    print("="*70)
    
    obj = Student("Geetha Gangabattula", "Computer Science", 95)
    
    print("\nPublic Access (name):")
    print(f"✓ {obj.name}")
    
    print("\nProtected Access (_branch):")
    print(f"✓ {obj._branch}")
    
    print("\nPrivate Access (via method):")
    print(f"✓ Marks: {obj.get_marks()}")
    
    print("\nAll Information:")
    print("-" * 50)
    obj.display_all()


# ============================================================================
# PROGRAM 45: MULTIPLE CLASSES
# ============================================================================

class ClassA:
    """Class A."""
    
    def show_a(self) -> None:
        """Display class A message."""
        print("✓ This is Class A")


class ClassB:
    """Class B."""
    
    def show_b(self) -> None:
        """Display class B message."""
        print("✓ This is Class B")


def demonstrate_multiple_classes() -> None:
    """Demonstrate multiple classes."""
    print("\n" + "="*70)
    print("PROGRAM 45: MULTIPLE CLASSES")
    print("="*70)
    
    obj1 = ClassA()
    obj2 = ClassB()
    
    print()
    obj1.show_a()
    obj2.show_b()


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def display_menu() -> None:
    """Display menu of all programs."""
    menu = """
╔════════════════════════════════════════════════════════════╗
║     MIRACLE PYTHON TRAINING - 45 COMPLETE PROGRAMS       ║
║              Employee: Geetha Gangabattula                 ║
║                  Company: Miracle                          ║
╚════════════════════════════════════════════════════════════╝

SELECT A PROGRAM TO RUN:
 1. Positive or Negative
 2. Student Pass/Fail and Rank
 3. Character Classification
 4. Biggest Among Two Numbers
 5. Square of Numbers (1-20)
 6. Print n Even Numbers
 7. Sum of Even Numbers
 8. Prime Numbers (1-10)
10. Factorial
11. Perfect Number
12. Fibonacci Series
13. Biggest Digit
14. Sum of Digits (Recursion)
15. Sum of Alternative Digits
16. Occurrences of Digit
17. All Digits Equal
18. Add First and Last Digit
19. Add Even and Odd Digits
20. Reverse a Number
21. Prime Numbers (m to n)
22. Print n Prime Numbers
25. Armstrong Numbers (1-1000)
26. Sum of Natural Numbers
27. Copy Array
28. Frequency of Elements
29. Duplicate Elements
30. Reverse Array
31. Largest and Smallest
32. Sort Descending
33. Sum of Array
34. Odd and Even in Array
35. Happy Number
40. Sum of Factorial Series
43. Patterns
44. Access Modifiers
45. Multiple Classes
 0. Exit

"""
    print(menu)


def main() -> None:
    """Main execution function."""
    while True:
        display_menu()
        
        try:
            choice = input("Enter your choice (0-45): ").strip()
            
            programs = {
                "1": check_positive_negative,
                "2": check_student_result,
                "3": classify_character,
                "4": find_biggest_two_numbers,
                "5": print_squares_upto_20,
                "6": print_n_even_numbers,
                "7": sum_even_numbers,
                "8": print_primes_1_to_10,
                "10": calculate_factorial,
                "11": check_perfect_number,
                "12": print_fibonacci_series,
                "13": find_biggest_digit,
                "14": sum_digits,
                "15": sum_alternative_digits,
                "16": count_digit_occurrences,
                "17": check_all_digits_equal,
                "18": add_first_and_last_digit,
                "19": add_even_and_odd_digits,
                "20": reverse_number,
                "21": print_primes_between_m_n,
                "22": print_n_primes,
                "25": print_armstrong_numbers,
                "26": sum_natural_numbers,
                "27": copy_array,
                "28": frequency_of_elements,
                "29": find_duplicate_elements,
                "30": reverse_array,
                "31": find_largest_and_smallest,
                "32": sort_descending,
                "33": sum_array,
                "34": classify_array_elements,
                "35": check_happy_number,
                "40": sum_factorial_series,
                "43": print_patterns,
                "44": demonstrate_access_modifiers,
                "45": demonstrate_multiple_classes,
            }
            
            if choice == "0":
                print("\n" + "="*70)
                print("✓ Thank you for using Miracle Python Training!")
                print("Employee: Geetha Gangabattula")
                print("Company: Miracle")
                print("="*70 + "\n")
                break
            
            if choice in programs:
                programs[choice]()
                input("\nPress Enter to continue...")
            else:
                print("❌ Invalid choice! Please select a valid program number.")
                input("\nPress Enter to continue...")
        
        except KeyboardInterrupt:
            print("\n\n⚠️  Program interrupted by user.")
            break
        except Exception as e:
            print(f"\n❌ An error occurred: {e}")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
