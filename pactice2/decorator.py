def decor(func):
    def wrapper():
        print("Begining of wrapper")
        func()
        print("Ending of wrapper")
    return wrapper

@decor
def greet():
    print("bonjour , Namaste welcome to paris .")
    
greet()