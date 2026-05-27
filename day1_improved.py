"""
Miracle Python Training - Day 1 (Improved)
Employee Name: Geetha Gangabattula
Topic: Intermediate Python Programs
Status: Completed
Date: 2026-05-27

This module contains improved versions of Day 1 programs with:
- Proper error handling
- PEP 8 compliance
- Function-based structure
- Comprehensive documentation
- Type hints
"""

from typing import Tuple, List

# ============================================================================
# CONSTANTS
# ============================================================================

DISTINCTION_GRADE = 75
PASS_GRADE = 50
INITIAL_BALANCE = 10000
SUBJECTS = ["Python", "Java", "DBMS"]
VALID_USERNAME = "geetha"
VALID_PASSWORD = "1234"
TABLE_RANGE = 11


# ============================================================================
# PROGRAM 1: STUDENT RESULT PROGRAM
# ============================================================================

def get_valid_integer(prompt: str, min_val: int = 0, max_val: int = 100) -> int:
    """
    Get validated integer input from user.
    
    Args:
        prompt (str): Message to display to user
        min_val (int): Minimum acceptable value (default: 0)
        max_val (int): Maximum acceptable value (default: 100)
    
    Returns:
        int: Valid integer within specified range
    
    Raises:
        ValueError: If input cannot be converted to integer
    """
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"❌ Please enter a number between {min_val} and {max_val}\n")
        except ValueError:
            print("❌ Please enter a valid number\n")


def get_student_marks() -> Tuple[str, int, int, int]:
    """
    Get student name and marks for all subjects.
    
    Returns:
        Tuple[str, int, int, int]: Student name and marks for 3 subjects
    """
    print("\n" + "="*50)
    print("PROGRAM 1: STUDENT RESULT PROGRAM")
    print("="*50)
    
    name = input("Enter Student Name: ").strip()
    
    if not name:
        print("❌ Name cannot be empty")
        return get_student_marks()
    
    marks = []
    for subject in SUBJECTS:
        mark = get_valid_integer(f"Enter {subject} Marks (0-100): ")
        marks.append(mark)
    
    return name, marks[0], marks[1], marks[2]


def calculate_result(average: float) -> str:
    """
    Determine student result based on average marks.
    
    Args:
        average (float): Average marks of student
    
    Returns:
        str: Result (Distinction, Pass, or Fail)
    """
    if average >= DISTINCTION_GRADE:
        return "Distinction"
    elif average >= PASS_GRADE:
        return "Pass"
    else:
        return "Fail"


def display_student_result(name: str, sub1: int, sub2: int, sub3: int) -> None:
    """
    Calculate and display student result.
    
    Args:
        name (str): Student name
        sub1 (int): Python marks
        sub2 (int): Java marks
        sub3 (int): DBMS marks
    """
    total = sub1 + sub2 + sub3
    average = total / 3
    result = calculate_result(average)
    
    print("\n" + "-"*50)
    print("RESULT")
    print("-"*50)
    print(f"Student Name    : {name}")
    print(f"Total Marks     : {total}")
    print(f"Average Marks   : {average:.2f}")
    print(f"Result          : {result} ✓")
    print("-"*50 + "\n")


# ============================================================================
# PROGRAM 2: ATM WITHDRAW PROGRAM
# ============================================================================

def validate_amount(amount: int, balance: int) -> bool:
    """
    Validate withdrawal amount.
    
    Args:
        amount (int): Amount to withdraw
        balance (int): Current account balance
    
    Returns:
        bool: True if amount is valid, False otherwise
    """
    if amount <= 0:
        print("❌ Amount must be greater than 0\n")
        return False
    
    if amount > balance:
        print(f"❌ Insufficient Balance. Available: ${balance}\n")
        return False
    
    return True


def atm_withdraw() -> None:
    """
    Process ATM withdrawal with validation and balance update.
    """
    print("\n" + "="*50)
    print("PROGRAM 2: ATM WITHDRAW PROGRAM")
    print("="*50)
    
    balance = INITIAL_BALANCE
    print(f"\nInitial Balance: ${balance}")
    
    while True:
        try:
            amount = int(input("Enter Withdraw Amount: $"))
            
            if validate_amount(amount, balance):
                balance -= amount
                print("\n" + "-"*50)
                print("✓ Transaction Successful!")
                print("-"*50)
                print(f"Amount Withdrawn    : ${amount}")
                print(f"Available Balance   : ${balance}")
                print("-"*50 + "\n")
                break
        except ValueError:
            print("❌ Please enter a valid amount\n")


# ============================================================================
# PROGRAM 3: LOGIN PROGRAM
# ============================================================================

def validate_credentials(username: str, password: str) -> bool:
    """
    Validate user credentials.
    
    Args:
        username (str): Username to validate
        password (str): Password to validate
    
    Returns:
        bool: True if credentials match, False otherwise
    """
    return username == VALID_USERNAME and password == VALID_PASSWORD


def login_program() -> None:
    """
    Process user login with credentials validation.
    """
    print("\n" + "="*50)
    print("PROGRAM 3: LOGIN PROGRAM")
    print("="*50 + "\n")
    
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        username = input("Enter Username: ").strip()
        password = input("Enter Password: ").strip()
        
        if validate_credentials(username, password):
            print("\n" + "-"*50)
            print(f"✓ Login Successful! Welcome, {username}")
            print("-"*50 + "\n")
            return
        
        attempts += 1
        remaining = max_attempts - attempts
        
        if remaining > 0:
            print(f"❌ Invalid Username or Password")
            print(f"⚠️  Remaining Attempts: {remaining}\n")
        else:
            print("❌ Maximum Login Attempts Exceeded. Account Locked!")
            print()


# ============================================================================
# PROGRAM 4: MULTIPLICATION TABLE
# ============================================================================

def get_valid_table_number() -> int:
    """
    Get valid number for multiplication table.
    
    Returns:
        int: Valid positive number
    """
    while True:
        try:
            number = int(input("Enter a Number: "))
            if number > 0:
                return number
            print("❌ Please enter a positive number\n")
        except ValueError:
            print("❌ Please enter a valid number\n")


def display_multiplication_table(number: int) -> None:
    """
    Display multiplication table for given number.
    
    Args:
        number (int): Number for which table is to be displayed
    """
    print("\n" + "="*50)
    print("PROGRAM 4: MULTIPLICATION TABLE")
    print("="*50)
    print(f"\nMultiplication Table of {number}:\n")
    print("-"*50)
    
    for i in range(1, TABLE_RANGE):
        result = number * i
        print(f"{number:3d} × {i:2d} = {result:5d}")
    
    print("-"*50 + "\n")


# ============================================================================
# PROGRAM 5: EVEN AND ODD NUMBERS
# ============================================================================

def classify_numbers(start: int, end: int) -> Tuple[List[int], List[int]]:
    """
    Classify numbers into even and odd.
    
    Args:
        start (int): Start of range
        end (int): End of range
    
    Returns:
        Tuple[List[int], List[int]]: Lists of even and odd numbers
    """
    even_numbers = [i for i in range(start, end + 1) if i % 2 == 0]
    odd_numbers = [i for i in range(start, end + 1) if i % 2 != 0]
    
    return even_numbers, odd_numbers


def display_even_odd_numbers(start: int = 1, end: int = 10) -> None:
    """
    Display even and odd numbers in a given range.
    
    Args:
        start (int): Start of range (default: 1)
        end (int): End of range (default: 10)
    """
    print("\n" + "="*50)
    print("PROGRAM 5: EVEN AND ODD NUMBERS")
    print("="*50)
    
    even_nums, odd_nums = classify_numbers(start, end)
    
    print(f"\nNumbers from {start} to {end}:\n")
    print("-"*50)
    
    print(f"Even Numbers: {even_nums}")
    print(f"Odd Numbers:  {odd_nums}")
    
    print("\nDetailed Classification:\n")
    
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(f"{i:2d} is Even Number ✓")
        else:
            print(f"{i:2d} is Odd Number ✓")
    
    print("-"*50 + "\n")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def display_header() -> None:
    """Display program header."""
    print("\n" + "="*50)
    print("MIRACLE PYTHON TRAINING - DAY 1 (IMPROVED)")
    print("="*50)
    print("Employee Name : Geetha Gangabattula")
    print("Company Name  : Miracle")
    print("="*50 + "\n")


def display_footer() -> None:
    """Display program footer."""
    print("\n" + "="*50)
    print("ALL PROGRAMS COMPLETED SUCCESSFULLY ✓")
    print("="*50)
    print("Employee Name : Geetha Gangabattula")
    print("Company Name  : Miracle")
    print("="*50 + "\n")


def main() -> None:
    """
    Execute all programs.
    """
    display_header()
    
    try:
        # Program 1: Student Result
        name, sub1, sub2, sub3 = get_student_marks()
        display_student_result(name, sub1, sub2, sub3)
        
        # Program 2: ATM Withdraw
        atm_withdraw()
        
        # Program 3: Login
        login_program()
        
        # Program 4: Multiplication Table
        number = get_valid_table_number()
        display_multiplication_table(number)
        
        # Program 5: Even and Odd Numbers
        display_even_odd_numbers()
        
        display_footer()
    
    except KeyboardInterrupt:
        print("\n\n⚠️  Program interrupted by user.")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
