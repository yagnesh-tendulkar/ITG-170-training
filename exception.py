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
