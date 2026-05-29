#arbitraryArguments
def key(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")
key(22, "BAlaji", greet="namasthe")



# def my_function(animal, name, age):
#   print("I have a", age, "year old", animal, "named", name)

# my_function("dog", name = "Buddy", age = 5) 