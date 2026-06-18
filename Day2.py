"""
Miracle Python Training - Day 2 (Improved)
Employee Name: Geetha Gangabattula
Topic: Python Basics and Intermediate Programs
Status: Completed
Date: 2026-05-27

This module contains improved versions of Day 2 programs with:
- Proper error handling
- PEP 8 compliance
- Function-based structure
- Comprehensive documentation
- Type hints
- Input validation
"""

import datetime
from typing import Tuple

# ============================================================================
# CONSTANTS
# ============================================================================

MIN_YEAR = 1900
MAX_YEAR = datetime.date.today().year
MIN_PRICE = 0.0
MIN_QUANTITY = 1


# ============================================================================
# PROGRAM 1: PERSONAL DETAILS PROGRAM
# ============================================================================

def get_personal_details() -> Tuple[str, str, str, str, str]:
    """
    Get personal details from user.
    
    Returns:
        Tuple[str, str, str, str, str]: Name, city, food, color, hobby
    """
    print("\n" + "="*60)
    print("PROGRAM 1: PERSONAL DETAILS PROGRAM")
    print("="*60)
    
    name = input("Enter Your Name: ").strip()
    if not name:
        print("❌ Name cannot be empty")
        return get_personal_details()
    
    city = input("Enter Your City: ").strip()
    if not city:
        print("❌ City cannot be empty")
        return get_personal_details()
    
    fav_food = input("Enter Favorite Food: ").strip()
    fav_color = input("Enter Favorite Color: ").strip()
    fav_hobby = input("Enter Favorite Hobby: ").strip()
    
    return name, city, fav_food, fav_color, fav_hobby


def display_personal_details(name: str, city: str, fav_food: str, 
                             fav_color: str, fav_hobby: str) -> None:
    """
    Display personal details.
    
    Args:
        name (str): Person's name
        city (str): Person's city
        fav_food (str): Favorite food
        fav_color (str): Favorite color
        fav_hobby (str): Favorite hobby
    """
    today = datetime.date.today()
    
    print("\n" + "-"*60)
    print("PERSONAL INFORMATION")
    print("-"*60)
    print(f"Your Name          : {name}")
    print(f"Your City          : {city}")
    print(f"Today's Date       : {today}")
    print(f"Favorite Food      : {fav_food}")
    print(f"Favorite Color     : {fav_color}")
    print(f"Favorite Hobby     : {fav_hobby}")
    print("-"*60 + "\n")


# ============================================================================
# PROGRAM 2: CALCULATOR PROGRAM
# ============================================================================

def get_valid_float(prompt: str, min_val: float = None) -> float:
    """
    Get validated float input from user.
    
    Args:
        prompt (str): Message to display
        min_val (float): Minimum acceptable value (optional)
    
    Returns:
        float: Valid float number
    """
    while True:
        try:
            value = float(input(prompt))
            if min_val is not None and value < min_val:
                print(f"❌ Value must be >= {min_val}\n")
                continue
            return value
        except ValueError:
            print("❌ Please enter a valid number\n")


def perform_calculations(a: float, b: float) -> None:
    """
    Perform basic arithmetic calculations.
    
    Args:
        a (float): First number
        b (float): Second number
    """
    print("\n" + "="*60)
    print("PROGRAM 2: CALCULATOR PROGRAM")
    print("="*60)
    
    sum_result = a + b
    diff_result = a - b
    product_result = a * b
    
    print("\n" + "-"*60)
    print("CALCULATION RESULTS")
    print("-"*60)
    print(f"First Number    : {a}")
    print(f"Second Number   : {b}")
    print(f"Sum             : {sum_result}")
    print(f"Difference      : {diff_result}")
    print(f"Product         : {product_result}")
    
    if b != 0:
        division_result = a / b
        print(f"Division        : {division_result:.2f}")
    else:
        print(f"Division        : Undefined (Cannot divide by 0)")
    
    print("-"*60 + "\n")


# ============================================================================
# PROGRAM 3: STRING CREATION PROGRAM
# ============================================================================

def demonstrate_string_types() -> None:
    """Display different types of string creation in Python."""
    print("\n" + "="*60)
    print("PROGRAM 3: STRING CREATION PROGRAM")
    print("="*60)
    
    # Single quote string
    s1 = "This is Single Quote String"
    
    # Double quote string
    s2 = "This is Double Quote String"
    
    # Triple quote string (multiline)
    s3 = """This is
Triple Quote
String"""
    
    print("\n" + "-"*60)
    print("DIFFERENT STRING TYPES")
    print("-"*60)
    
    print("\n✓ Single Quote String:")
    print(s1)
    
    print("\n✓ Double Quote String:")
    print(s2)
    
    print("\n✓ Triple Quote String (Multiline):")
    print(s3)
    
    print("\n" + "-"*60 + "\n")


# ============================================================================
# PROGRAM 4: COMPARE TWO NUMBERS
# ============================================================================

def compare_numbers(x: float, y: float) -> None:
    """
    Compare two numbers and display result.
    
    Args:
        x (float): First number
        y (float): Second number
    """
    print("\n" + "="*60)
    print("PROGRAM 4: COMPARE TWO NUMBERS")
    print("="*60)
    
    print("\n" + "-"*60)
    print("COMPARISON RESULT")
    print("-"*60)
    
    if x > y:
        print(f"✓ {x} is Greater than {y}")
        difference = x - y
        print(f"  Difference: {difference}")
    elif y > x:
        print(f"✓ {y} is Greater than {x}")
        difference = y - x
        print(f"  Difference: {difference}")
    else:
        print(f"✓ Both Numbers are Equal: {x} = {y}")
    
    print("-"*60 + "\n")


# ============================================================================
# PROGRAM 5: INTRODUCTION PARAGRAPH PROGRAM
# ============================================================================

def display_introduction() -> None:
    """Display introduction paragraph."""
    print("\n" + "="*60)
    print("PROGRAM 5: INTRODUCTION PARAGRAPH")
    print("="*60)
    
    intro = """
Hello,
My name is Geetha Gangabattula.

I am learning Python Programming.
I enjoy coding and building projects.
I want to become a Full Stack Developer.
"""
    
    print("\n" + "-"*60)
    print(intro)
    print("-"*60 + "\n")


# ============================================================================
# PROGRAM 6: BOOK BILL PROGRAM
# ============================================================================

def get_valid_integer(prompt: str, min_val: int = 1) -> int:
    """
    Get validated integer input from user.
    
    Args:
        prompt (str): Message to display
        min_val (int): Minimum acceptable value (default: 1)
    
    Returns:
        int: Valid integer
    """
    while True:
        try:
            value = int(input(prompt))
            if value >= min_val:
                return value
            print(f"❌ Value must be >= {min_val}\n")
        except ValueError:
            print("❌ Please enter a valid number\n")


def calculate_book_bill(price: float, quantity: int) -> None:
    """
    Calculate total book bill.
    
    Args:
        price (float): Price of single book
        quantity (int): Number of books
    """
    print("\n" + "="*60)
    print("PROGRAM 6: BOOK BILL PROGRAM")
    print("="*60)
    
    total_cost = price * quantity
    
    print("\n" + "-"*60)
    print("BILL DETAILS")
    print("-"*60)
    print(f"Book Price per Unit : ${price:.2f}")
    print(f"Quantity            : {quantity}")
    print(f"Total Cost          : ${total_cost:.2f}")
    print("-"*60 + "\n")


# ============================================================================
# PROGRAM 7: AGE CALCULATOR PROGRAM
# ============================================================================

def calculate_age(birth_year: int) -> None:
    """
    Calculate age based on birth year.
    
    Args:
        birth_year (int): Year of birth
    """
    print("\n" + "="*60)
    print("PROGRAM 7: AGE CALCULATOR PROGRAM")
    print("="*60)
    
    current_year = datetime.date.today().year
    age = current_year - birth_year
    
    # Validate age
    if age < 0:
        print("\n❌ Birth year cannot be in the future!")
        return
    
    if age > 150:
        print("\n⚠️ Please check your birth year!")
        return
    
    print("\n" + "-"*60)
    print("AGE CALCULATION")
    print("-"*60)
    print(f"Birth Year    : {birth_year}")
    print(f"Current Year  : {current_year}")
    print(f"Your Age      : {age} years")
    print("-"*60 + "\n")


# ============================================================================
# PROGRAM 8: NAME TRANSFORMATION PROGRAM
# ============================================================================

def transform_name(user_name: str) -> None:
    """
    Transform name to different cases and display length.
    
    Args:
        user_name (str): Name to transform
    """
    print("\n" + "="*60)
    print("PROGRAM 8: NAME TRANSFORMATION PROGRAM")
    print("="*60)
    
    uppercase_name = user_name.upper()
    lowercase_name = user_name.lower()
    name_length = len(user_name)
    title_case = user_name.title()
    char_count = len(user_name.replace(" ", ""))
    
    print("\n" + "-"*60)
    print("NAME TRANSFORMATIONS")
    print("-"*60)
    print(f"Original Name          : {user_name}")
    print(f"Uppercase Name         : {uppercase_name}")
    print(f"Lowercase Name         : {lowercase_name}")
    print(f"Title Case Name        : {title_case}")
    print(f"Total Length           : {name_length} characters")
    print(f"Characters (no spaces) : {char_count}")
    print("-"*60 + "\n")


# ============================================================================
# PROGRAM 9: TEMPERATURE CONVERSION PROGRAM
# ============================================================================

def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convert temperature from Celsius to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius
    
    Returns:
        float: Temperature in Fahrenheit
    """
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Convert temperature from Fahrenheit to Celsius.
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit
    
    Returns:
        float: Temperature in Celsius
    """
    return (fahrenheit - 32) * 5 / 9


def convert_temperature(celsius: float) -> None:
    """
    Convert temperature and display results.
    
    Args:
        celsius (float): Temperature in Celsius
    """
    print("\n" + "="*60)
    print("PROGRAM 9: TEMPERATURE CONVERSION")
    print("="*60)
    
    fahrenheit = celsius_to_fahrenheit(celsius)
    
    print("\n" + "-"*60)
    print("TEMPERATURE CONVERSION")
    print("-"*60)
    print(f"Celsius Temperature    : {celsius}°C")
    print(f"Fahrenheit Temperature : {fahrenheit:.2f}°F")
    print("-"*60 + "\n")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def display_header() -> None:
    """Display program header."""
    print("\n" + "="*60)
    print("MIRACLE PYTHON TRAINING - DAY 2 (IMPROVED)")
    print("="*60)
    print("Employee Name : Geetha Gangabattula")
    print("Company Name  : Miracle")
    print("="*60)


def display_footer() -> None:
    """Display program footer."""
    print("\n" + "="*60)
    print("ALL DAY 2 PROGRAMS COMPLETED SUCCESSFULLY ✓")
    print("="*60)
    print("Employee Name : Geetha Gangabattula")
    print("Company Name  : Miracle")
    print("="*60 + "\n")


def main() -> None:
    """Execute all Day 2 programs."""
    display_header()
    
    try:
        # Program 1: Personal Details
        name, city, food, color, hobby = get_personal_details()
        display_personal_details(name, city, food, color, hobby)
        
        # Program 2: Calculator
        a = get_valid_float("Enter First Number: ")
        b = get_valid_float("Enter Second Number: ")
        perform_calculations(a, b)
        
        # Program 3: String Creation
        demonstrate_string_types()
        
        # Program 4: Compare Numbers
        x = get_valid_float("Enter First Number: ")
        y = get_valid_float("Enter Second Number: ")
        compare_numbers(x, y)
        
        # Program 5: Introduction
        display_introduction()
        
        # Program 6: Book Bill
        price = get_valid_float("Enter Book Price ($): ", MIN_PRICE)
        quantity = get_valid_integer("Enter Quantity: ", MIN_QUANTITY)
        calculate_book_bill(price, quantity)
        
        # Program 7: Age Calculator
        birth_year = get_valid_integer("Enter Birth Year: ", MIN_YEAR)
        calculate_age(birth_year)
        
        # Program 8: Name Transformation
        user_name = input("Enter Your Name: ").strip()
        if user_name:
            transform_name(user_name)
        else:
            print("❌ Name cannot be empty")
        
        # Program 9: Temperature Conversion
        celsius = float(input("Enter Temperature in Celsius: "))
        convert_temperature(celsius)
        
        display_footer()
    
    except KeyboardInterrupt:
        print("\n\n⚠️  Program interrupted by user.")
    except ValueError as e:
        print(f"\n❌ Invalid input: {e}")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
