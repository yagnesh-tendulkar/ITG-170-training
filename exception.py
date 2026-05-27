# Custom Exception Classes
class InsufficientFundsException(Exception):
    """Custom exception for insufficient funds."""
    def __init__(self, balance: float, amount: float):
        self.balance = balance
        self.amount = amount
        super().__init__(...)

# Complete Exception Handling
try:
    risky_operation()
except ZeroDivisionError:
    print("✓ Exception Handled")
except ValueError:
    print("✓ ValueError Handled")
else:
    print("✓ No exception occurred")
finally:
    print("✓ Always executes")

# Exception Chaining
try:
    value = int(data)
except ValueError as e:
    raise RuntimeError(f"Failed: {e}") from e
"""
Miracle Python Training - Exception Handling (Improved)
Employee Name: Geetha Gangabattula
Topic: Python Exception Handling with Best Practices
Status: Completed
Date: 2026-05-27

This module demonstrates proper exception handling with:
- Try-except blocks
- Multiple exception handlers
- Nested try blocks
- Finally blocks
- Custom exceptions
- Exception raising
- Best practices
- Comprehensive error handling
"""

import sys
from typing import Optional


# ============================================================================
# PROGRAM 1: TRY-EXCEPT BLOCK (BASIC EXCEPTION HANDLING)
# ============================================================================

def demo_basic_try_except() -> None:
    """
    Demonstrate basic try-except block for handling exceptions.
    
    This example shows how to catch a ZeroDivisionError when
    attempting to divide by zero.
    
    Returns:
        None
    """
    print("\n" + "="*70)
    print("PROGRAM 1: BASIC TRY-EXCEPT BLOCK")
    print("="*70)
    
    try:
        print("\nAttempting to divide 10 by 0...")
        a = 10 / 0
        print(f"Result: {a}")
    
    except ZeroDivisionError:
        print("✓ Exception Handled: Cannot divide by zero!")
    
    print("-"*70 + "\n")


# ============================================================================
# PROGRAM 2: MULTIPLE EXCEPT BLOCKS
# ============================================================================

def demo_multiple_except_blocks() -> None:
    """
    Demonstrate multiple except blocks for handling different exceptions.
    
    This example shows how to catch different types of exceptions
    (ValueError and ZeroDivisionError) in separate except blocks.
    
    Returns:
        None
    """
    print("\n" + "="*70)
    print("PROGRAM 2: MULTIPLE EXCEPT BLOCKS")
    print("="*70)
    
    # Example 1: ValueError
    print("\nExample 1: ValueError")
    print("-"*70)
    
    try:
        print("Attempting to convert 'hello' to integer...")
        num = int("hello")
        print(f"Converted value: {num}")
    
    except ValueError:
        print("✓ ValueError Handled: Cannot convert 'hello' to integer!")
    
    except ZeroDivisionError:
        print("ZeroDivisionError Handled")
    
    # Example 2: ZeroDivisionError
    print("\nExample 2: ZeroDivisionError")
    print("-"*70)
    
    try:
        print("Attempting to divide 10 by 0...")
        a = 10 / 0
        print(f"Result: {a}")
    
    except ValueError:
        print("ValueError Handled")
    
    except ZeroDivisionError:
        print("✓ ZeroDivisionError Handled: Cannot divide by zero!")
    
    print("-"*70 + "\n")


# ============================================================================
# PROGRAM 3: NESTED TRY BLOCKS
# ============================================================================

def demo_nested_try_blocks() -> None:
    """
    Demonstrate nested try-except blocks.
    
    This example shows how inner try blocks can catch specific exceptions,
    while outer try blocks can catch exceptions from inner blocks.
    
    Returns:
        None
    """
    print("\n" + "="*70)
    print("PROGRAM 3: NESTED TRY BLOCKS")
    print("="*70)
    
    try:
        print("\nEntering outer try block...")
        
        try:
            print("Entering inner try block...")
            print("Attempting to divide 10 by 0...")
            a = 10 / 0
            print(f"Result: {a}")
        
        except ZeroDivisionError:
            print("✓ Inner Exception Handled: Cannot divide by zero!")
        
        except ValueError:
            print("Inner ValueError Handled")
        
        print("Exiting inner try block...")
    
    except Exception as e:
        print(f"✓ Outer Exception Caught: {type(e).__name__} - {e}")
    
    print("-"*70 + "\n")


# ============================================================================
# PROGRAM 4: FINALLY BLOCK
# ============================================================================

def demo_finally_block() -> None:
    """
    Demonstrate finally block execution.
    
    The finally block always executes regardless of whether
    an exception was raised or caught.
    
    Returns:
        None
    """
    print("\n" + "="*70)
    print("PROGRAM 4: FINALLY BLOCK")
    print("="*70)
    
    print("\nExample 1: With Exception")
    print("-"*70)
    
    try:
        print("Attempting to divide 10 by 0...")
        a = 10 / 0
        print(f"Result: {a}")
    
    except ZeroDivisionError:
        print("✓ Exception Caught: Cannot divide by zero!")
    
    finally:
        print("✓ Finally Block Executed (always runs)")
    
    print("\nExample 2: Without Exception")
    print("-"*70)
    
    try:
        print("Performing normal division: 10 / 2...")
        a = 10 / 2
        print(f"Result: {a}")
    
    except ZeroDivisionError:
        print("Exception Caught")
    
    finally:
        print("✓ Finally Block Executed (always runs)")
    
    print("-"*70 + "\n")


# ============================================================================
# PROGRAM 5: RAISE KEYWORD (CUSTOM EXCEPTIONS)
# ============================================================================

def check_eligibility(age: int) -> None:
    """
    Check if person is eligible based on age.
    
    Demonstrates raising custom exceptions when conditions are not met.
    
    Args:
        age (int): Age of the person
    
    Returns:
        None
    
    Raises:
        Exception: If age is less than 18
    
    Example:
        >>> check_eligibility(15)
        Traceback (most recent call last):
          ...
        Exception: ❌ Not Eligible: Age must be 18 or above
    """
    print(f"\nChecking eligibility for age: {age}...")
    
    try:
        if age < 0:
            raise ValueError("❌ Age cannot be negative")
        
        elif age < 18:
            raise Exception(f"❌ Not Eligible: Age must be 18 or above (Current: {age})")
        
        else:
            print(f"✓ Eligible: Age {age} is valid")
    
    except Exception as e:
        print(f"✓ Exception Caught: {e}")


def demo_raise_keyword() -> None:
    """
    Demonstrate raising and catching custom exceptions.
    
    Returns:
        None
    """
    print("\n" + "="*70)
    print("PROGRAM 5: RAISE KEYWORD (CUSTOM EXCEPTIONS)")
    print("="*70)
    
    # Test Case 1: Not Eligible
    print("\nTest Case 1: Age Too Young")
    print("-"*70)
    check_eligibility(15)
    
    # Test Case 2: Eligible
    print("\nTest Case 2: Age Eligible")
    print("-"*70)
    check_eligibility(25)
    
    # Test Case 3: Negative Age
    print("\nTest Case 3: Invalid Age")
    print("-"*70)
    check_eligibility(-5)
    
    print("-"*70 + "\n")


# ============================================================================
# PROGRAM 6: FUNCTION EXCEPTION HANDLING
# ============================================================================

def risky_operation() -> Optional[float]:
    """
    Perform a risky operation that may raise an exception.
    
    This function demonstrates how exceptions from functions
    propagate to the caller.
    
    Returns:
        Optional[float]: Result of division, or None if error occurs
    
    Raises:
        ZeroDivisionError: When attempting to divide by zero
    """
    print("Inside risky_operation(): Attempting to divide 10 by 0...")
    a = 10 / 0  # This will raise ZeroDivisionError
    return a


def demo_function_exception_handling() -> None:
    """
    Demonstrate exception handling for function calls.
    
    Shows how to catch exceptions raised by functions.
    
    Returns:
        None
    """
    print("\n" + "="*70)
    print("PROGRAM 6: FUNCTION EXCEPTION HANDLING")
    print("="*70)
    
    try:
        print("\nCalling risky_operation()...")
        result = risky_operation()
        print(f"Result: {result}")
    
    except ZeroDivisionError:
        print("✓ Exception Handled: Function raised ZeroDivisionError")
    
    except Exception as e:
        print(f"✓ Exception Handled: {type(e).__name__} - {e}")
    
    print("-"*70 + "\n")


# ============================================================================
# PROGRAM 7: CUSTOM EXCEPTION CLASSES
# ============================================================================

class InsufficientFundsException(Exception):
    """Custom exception for insufficient funds."""
    
    def __init__(self, balance: float, amount: float) -> None:
        """
        Initialize the exception.
        
        Args:
            balance (float): Current balance
            amount (float): Requested amount
        """
        self.balance = balance
        self.amount = amount
        self.message = (f"Insufficient funds! "
                       f"Available: ${balance:.2f}, "
                       f"Requested: ${amount:.2f}")
        super().__init__(self.message)


class InvalidAgeException(Exception):
    """Custom exception for invalid age."""
    
    def __init__(self, age: int) -> None:
        """
        Initialize the exception.
        
        Args:
            age (int): Invalid age value
        """
        self.age = age
        self.message = f"Invalid age: {age}. Age must be between 0 and 150."
        super().__init__(self.message)


def demo_custom_exceptions() -> None:
    """
    Demonstrate custom exception classes.
    
    Returns:
        None
    """
    print("\n" + "="*70)
    print("PROGRAM 7: CUSTOM EXCEPTION CLASSES")
    print("="*70)
    
    # Example 1: Insufficient Funds
    print("\nExample 1: Insufficient Funds Exception")
    print("-"*70)
    
    try:
        balance = 500.00
        withdrawal = 1000.00
        
        if withdrawal > balance:
            raise InsufficientFundsException(balance, withdrawal)
        
        print(f"✓ Withdrawal successful: ${withdrawal:.2f}")
    
    except InsufficientFundsException as e:
        print(f"✓ Custom Exception Caught: {e}")
    
    # Example 2: Invalid Age
    print("\nExample 2: Invalid Age Exception")
    print("-"*70)
    
    try:
        age = 200
        
        if not (0 <= age <= 150):
            raise InvalidAgeException(age)
        
        print(f"✓ Age {age} is valid")
    
    except InvalidAgeException as e:
        print(f"✓ Custom Exception Caught: {e}")
    
    print("-"*70 + "\n")


# ============================================================================
# PROGRAM 8: ELSE AND EXCEPT TOGETHER
# ============================================================================

def demo_else_except() -> None:
    """
    Demonstrate else block with try-except.
    
    The else block executes only if no exception occurs.
    
    Returns:
        None
    """
    print("\n" + "="*70)
    print("PROGRAM 8: ELSE BLOCK WITH TRY-EXCEPT")
    print("="*70)
    
    print("\nExample 1: Exception Occurs")
    print("-"*70)
    
    try:
        print("Attempting invalid operation...")
        num = int("hello")
    
    except ValueError:
        print("✓ ValueError Caught")
    
    else:
        print("No exception occurred")
    
    print("\nExample 2: No Exception")
    print("-"*70)
    
    try:
        print("Attempting valid operation...")
        num = int("123")
        print(f"Converted value: {num}")
    
    except ValueError:
        print("ValueError Caught")
    
    else:
        print("✓ Else Block Executed: No exception occurred")
    
    print("-"*70 + "\n")


# ============================================================================
# PROGRAM 9: EXCEPTION CHAINING
# ============================================================================

def process_user_data(data: str) -> int:
    """
    Process user data with exception chaining.
    
    Args:
        data (str): Data to process
    
    Returns:
        int: Processed value
    
    Raises:
        ValueError: If data is invalid
        RuntimeError: If processing fails
    """
    try:
        print(f"Processing data: '{data}'...")
        value = int(data)
        
        if value < 0:
            raise ValueError("Value must be positive")
        
        return value
    
    except ValueError as e:
        raise RuntimeError(f"Failed to process data: {e}") from e


def demo_exception_chaining() -> None:
    """
    Demonstrate exception chaining.
    
    Returns:
        None
    """
    print("\n" + "="*70)
    print("PROGRAM 9: EXCEPTION CHAINING")
    print("="*70)
    
    test_cases = ["hello", "-5", "42"]
    
    for test_data in test_cases:
        print(f"\nTesting with data: '{test_data}'")
        print("-"*70)
        
        try:
            result = process_user_data(test_data)
            print(f"✓ Result: {result}")
        
        except RuntimeError as e:
            print(f"✓ RuntimeError Caught: {e}")
            print(f"  Root Cause: {type(e.__cause__).__name__}")
    
    print("-"*70 + "\n")


# ============================================================================
# PROGRAM 10: BEST PRACTICES
# ============================================================================

def demonstrate_best_practices() -> None:
    """
    Demonstrate exception handling best practices.
    
    Returns:
        None
    """
    print("\n" + "="*70)
    print("PROGRAM 10: EXCEPTION HANDLING BEST PRACTICES")
    print("="*70)
    
    print("\n✓ BEST PRACTICES:")
    print("-"*70)
    
    print("\n1. Catch Specific Exceptions:")
    print("   ✓ Good: except ValueError:")
    print("   ✗ Bad:  except:")
    
    print("\n2. Use Finally for Cleanup:")
    print("   ✓ Always use finally to close resources")
    print("   ✓ Example: file.close() in finally block")
    
    print("\n3. Provide Meaningful Messages:")
    print("   ✓ Include context and helpful information")
    
    print("\n4. Don't Suppress Exceptions Silently:")
    print("   ✗ Bad: except: pass")
    print("   ✓ Good: except Exception as e: print(f'Error: {e}')")
    
    print("\n5. Use Custom Exceptions:")
    print("   ✓ Create custom exceptions for application logic")
    
    print("\n6. Exception Hierarchy:")
    print("   ✓ BaseException")
    print("     └─ Exception")
    print("        ├─ ValueError")
    print("        ├─ TypeError")
    print("        ├─ ZeroDivisionError")
    print("        └─ ...custom exceptions")
    
    print("\n7. Use Type Hints:")
    print("   ✓ def function() -> Optional[int]:")
    print("   ✓ raise ValueError('message')")
    
    print("\n8. Log Exceptions:")
    print("   ✓ Use logging module for production code")
    
    print("\n" + "-"*70 + "\n")


# ============================================================================
# DEMONSTRATION OF COMMON EXCEPTIONS
# ============================================================================

def demo_common_exceptions() -> None:
    """
    Demonstrate common Python exceptions.
    
    Returns:
        None
    """
    print("\n" + "="*70)
    print("COMMON PYTHON EXCEPTIONS")
    print("="*70)
    
    exceptions_info = [
        ("ValueError", "int('hello')", "Invalid value type"),
        ("ZeroDivisionError", "10 / 0", "Division by zero"),
        ("IndexError", "list[99]", "List index out of range"),
        ("KeyError", "dict['missing']", "Dictionary key not found"),
        ("TypeError", "'string' + 5", "Invalid type operation"),
        ("AttributeError", "obj.missing_attr", "Attribute not found"),
        ("FileNotFoundError", "open('missing.txt')", "File not found"),
    ]
    
    print("\nException Type          | Example Code         | Description")
    print("-"*70)
    
    for exc_type, example, description in exceptions_info:
        print(f"{exc_type:22} | {example:20} | {description}")
    
    print("-"*70 + "\n")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def display_menu() -> None:
    """Display menu of all programs."""
    menu = """
╔════════════════════════════════════════════════════════════╗
║   MIRACLE PYTHON TRAINING - EXCEPTION HANDLING MODULE      ║
║              Employee: Geetha Gangabattula                  ║
║                  Company: Miracle                           ║
╚════════════════════════════════════════════════════════════╝

SELECT A PROGRAM TO RUN:
 1. Basic Try-Except Block
 2. Multiple Except Blocks
 3. Nested Try Blocks
 4. Finally Block
 5. Raise Keyword (Custom Exceptions)
 6. Function Exception Handling
 7. Custom Exception Classes
 8. Else Block with Try-Except
 9. Exception Chaining
10. Exception Handling Best Practices
11. Common Python Exceptions
 0. Exit

"""
    print(menu)


def main() -> None:
    """Main execution function."""
    while True:
        display_menu()
        
        try:
            choice = input("Enter your choice (0-11): ").strip()
            
            programs = {
                "1": demo_basic_try_except,
                "2": demo_multiple_except_blocks,
                "3": demo_nested_try_blocks,
                "4": demo_finally_block,
                "5": demo_raise_keyword,
                "6": demo_function_exception_handling,
                "7": demo_custom_exceptions,
                "8": demo_else_except,
                "9": demo_exception_chaining,
                "10": demonstrate_best_practices,
                "11": demo_common_exceptions,
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
                input("Press Enter to continue...")
            else:
                print("\n❌ Invalid choice! Please select a valid program number.\n")
                input("Press Enter to continue...")
        
        except KeyboardInterrupt:
            print("\n\n⚠️  Program interrupted by user.")
            break
        except Exception as e:
            print(f"\n❌ An error occurred: {e}\n")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()
