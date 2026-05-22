 #1. Function to print a welcome message
def greet():
    print("Welcome! Hope you have a great day!")

greet()


# 2. Function that returns the larger of two numbers
def larger_number(a, b):
    return a if a > b else b

print("Larger number:", larger_number(10, 25))


# 3. Function that calculates the area of a rectangle
def rectangle_area(length, width):
    return length * width

print("Rectangle area:", rectangle_area(5, 4))


# 4. Function that accepts any number of numbers and returns their sum
def sum_numbers(*args):
    return sum(args)

print("Sum:", sum_numbers(1, 2, 3, 4, 5))


# 5. Function that returns the square of a number
def square(n):
    return n * n

print("Square:", square(6))


# 6. Function that checks if a number is even
def is_even(n):
    return n % 2 == 0

print("Is even (8):", is_even(8))
print("Is even (7):", is_even(7))


# 7. Function that greets a user using their name
def greet_user(name):
    print(f"Hello, {name}! Welcome!")

greet_user("Alex")


# 8. Function that finds the average of 3 numbers
def average_of_three(a, b, c):
    return (a + b + c) / 3

print("Average:", average_of_three(10, 20, 30))
