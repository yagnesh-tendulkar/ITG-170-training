# 1
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])


# 2
numbers = [x for x in range(1, 11)]
print("Numbers 1–10:", numbers)


# 3. Filter numbers greater than 5
nums = [2, 5, 7, 1, 9, 3, 10]
filtered = [x for x in nums if x > 5]
print("Numbers > 5:", filtered)


# 4. Dictionary storing name, age, course
student = {
    "Name": "John",
    "Age": 21,
    "Course": "Python"
}

print("\nStudent details:")
for key, value in student.items():
    print(key, ":", value)


# 5. Dictionary comprehension: squares of 1–5
squares = {x: x**2 for x in range(1, 6)}
print("\nSquares dictionary:", squares)


# 6. List of 5 favorite movies and print using loop
movies = ["Inception", "Interstellar", "Avengers", "Titanic", "Joker"]

print("\nMovies list:")
for movie in movies:
    print(movie)


# 7. Add and remove a movie
movies.append("Batman")
movies.remove("Titanic")

print("\nUpdated movies list:", movies)


# 8. Product dictionary and total cost calculation
product = {
    "name": "Book",
    "price": 200,
    "quantity": 3
}

total_cost = product["price"] * product["quantity"]
print("\nTotal cost:", total_cost)


# 9. List comprehension for odd numbers from 1–20
odds = [x for x in range(1, 21) if x % 2 != 0]
print("\nOdd numbers:", odds)


# 10. Filter names longer than 4 letters
names = ["John", "Alexander", "Emma", "Sophia", "Raj"]
long_names = [name for name in names if len(name) > 4]

print("\nNames longer than 4 letters:", long_names)
