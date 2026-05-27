# 1. Fruits Task
def fruits_task():
    fruits = ["Apple","Banana","PineApple","Mango","Grapes"]
    print("First fruit:", fruits[0])
    print("Last fruit:", fruits[-1])

# 2. Numbers Task
def numbers_task():
    num = [i for i in range(1,11)]
    print(num)

# 3. Filter Numbers
def filter_numbers():
    numbers = [2,5,7,1,9,3,10]
    ans = [i for i in numbers if i > 5]
    print(ans)

# 4. Dictionary Task
def dictionary_task():
    d = {"Name":"John","Age":25,"Course":"Python"}
    for k,v in d.items():
        print(k,v)

# 5. Squares Task
def squares_task():
    d = {i:i*i for i in range(1,6)}
    print(d)

# 6. Movies Task
def movies_task():
    movies = ["Inception","The Matrix","Interstellar","The Dark Knight","Pulp Fiction"]
    for movie in movies:
        print(movie)
    movies.append("The Lord of the Rings")
    movies.remove("Pulp Fiction")
    print(movies)

# 7. Product Task
def product_task():
    product = {"name":"Laptop","price":1000,"quantity":2}
    cost = product["price"] * product["quantity"]
    print("Total cost:", cost)

# 8. Odd Numbers Task
def odd_numbers_task():
    odd = [i for i in range(1,21) if i % 2 != 0]
    print(odd)

# 9. Names Task
def names_task():
    names = ["Alice","Bob","Charlie","David","Eve"]
    long_names = [name for name in names if len(name) > 4]
    print(long_names)

# User Choice
print("1. Fruits Task")
print("2. Numbers Task")
print("3. Filter Numbers")
print("4. Dictionary Task")
print("5. Squares Task")
print("6. Movies Task")
print("7. Product Task")
print("8. Odd Numbers Task")
print("9. Names Task")

choice = int(input("Enter your choice: "))

if choice == 1:
    fruits_task()
elif choice == 2:
    numbers_task()
elif choice == 3:
    filter_numbers()
elif choice == 4:
    dictionary_task()
elif choice == 5:
    squares_task()
elif choice == 6:
    movies_task()
elif choice == 7:
    product_task()
elif choice == 8:
    odd_numbers_task()
elif choice == 9:
    names_task()
else:
    print("Invalid Choice")