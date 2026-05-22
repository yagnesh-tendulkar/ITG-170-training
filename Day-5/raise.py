class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")

    print("You are eligible.")

except InvalidAgeError as e:
    print("Custom Exception:", e)

except ValueError:
    print("Please enter a valid number.")

finally:
    print("Program execution completed.")