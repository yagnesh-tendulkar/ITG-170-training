class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Robot:
    def speak(self):
        return "Beep Boop!"

def make_it_talk(thing):
    # DYNAMIC BINDING: Python looks for the 'speak' method 
    # ONLY when this line actually executes.
    print(f"Result: {thing.speak()}")

# --- 1. Dynamic Typing in Action ---
my_var = Dog()          # my_var is currently a Dog
make_it_talk(my_var)

my_var = Cat()          # Same variable name, now points to a Cat
make_it_talk(my_var)

# --- 2. Duck Typing (Dynamic Binding's Best Friend) ---
# Robot doesn't inherit from Animal, but it has a 'speak' method.
# Python binds it successfully anyway!
my_var = Robot()
make_it_talk(my_var)
