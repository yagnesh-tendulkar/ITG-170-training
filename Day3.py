# Function to print a welcome message
def greet():
    print("Welcome to Python Functions!")


greet()


# Function to return the larger number
def larger_number(a, b):
    if a > b:
        return a
    else:
        return b


print("Larger number:", larger_number(10, 20))


# Function to calculate the area of a rectangle
def rectangle_area(length, width):
    return length * width


print("Area of rectangle:", rectangle_area(5, 4))


# Function that accepts any number of numbers and returns their sum
def total_sum(*numbers):
    return sum(numbers)


print("Sum:", total_sum(10, 20, 30, 40))


# Function with a doc string
def square(num):
    """
    This function returns the square of a number.
    """
    return num * num


print("Square:", square(6))


# Function that checks if a number is even
def is_even(num):
    return num % 2 == 0


print("Is even:", is_even(8))


# Function that greets a user using their name
def greet_user(name):
    print("Hello,", name)


greet_user("Vennela")


# Function that finds the average of 3 numbers
def average(a, b, c):
    return (a + b + c) / 3


print("Average:", average(10, 20, 30))


# Another function with proper doc string
def add(a, b):
    """
    This function takes two numbers as input
    and returns their addition.
    """
    return a + b
print("Addition:", add(5, 7))

# Create a list of 5 fruits
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

# Print first and last fruit
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])


# List of numbers from 1–10 using list comprehension
numbers = [i for i in range(1, 11)]
print("Numbers from 1 to 10:", numbers)


# Filter only numbers greater than 5
num_list = [2, 5, 7, 1, 9, 3, 10]

greater_than_5 = [num for num in num_list if num > 5]

print("Numbers greater than 5:", greater_than_5)


# Create a dictionary
student = {
    "Name": "Vennela",
    "Age": 22,
    "Course": "MCA"
}

# Print all keys and values
print("\nDictionary Keys:")
for key in student.keys():
    print(key)

print("\nDictionary Values:")
for value in student.values():
    print(value)


# Dictionary comprehension for squares
squares = {x: x**2 for x in range(1, 6)}

print("\nSquares Dictionary:", squares)


# Create a list of 5 favorite movies
movies = ["RRR", "Bahubali", "KGF", "Pushpa", "Salaar"]

print("\nFavorite Movies:")
for movie in movies:
    print(movie)


# Add and remove a movie
movies.append("Leo")      # Add movie
movies.remove("KGF")      # Remove movie

print("\nUpdated Movie List:", movies)


# Product dictionary
product = {
    "name": "Laptop",
    "price": 50000,
    "quantity": 2
}

# Calculate total cost
total_cost = product["price"] * product["quantity"]

print("\nTotal Cost:", total_cost)


# List of odd numbers from 1–20
odd_numbers = [x for x in range(1, 21) if x % 2 != 0]

print("\nOdd Numbers:", odd_numbers)


# Filter names longer than 4 letters
names = ["Ram", "Vennela", "John", "Keerthi", "Sai"]

long_names = [name for name in names if len(name) > 4]

print("\nNames longer than 4 letters:", long_names)