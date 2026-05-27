# 1. Greet Function
def greet():
    print("Welcome to the Python programming course!")

# 2. Larger Number Function
def larger(a, b):
    if a > b:
        return a
    else:
        return b

# 3. Rectangle Area Function
def area(length, width):
    return length * width

# 4. Sum Function
def sum_numbers(*args):
    return sum(args)

# 5. Square Function
def square(n):
    """This function returns the square of a number."""
    return n ** 2

# 6. Even Check Function
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# 7. Greet User Function
def greet_user(name):
    print(f"Hello, {name}!")

# Menu
print("1. Greet Function")
print("2. Larger Number")
print("3. Rectangle Area")
print("4. Sum Numbers")
print("5. Square Number")
print("6. Check Even")
print("7. Greet User")

choice = int(input("Enter your choice: "))

if choice == 1:
    greet()

elif choice == 2:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(larger(a, b))

elif choice == 3:
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    print(area(length, width))

elif choice == 4:
    print(sum_numbers(1, 2, 3, 4, 5))

elif choice == 5:
    n = int(input("Enter number: "))
    print(square(n))

elif choice == 6:
    n = int(input("Enter number: "))
    print(is_even(n))

elif choice == 7:
    name = input("Enter your name: ")
    greet_user(name)

else:
    print("Invalid Choice")