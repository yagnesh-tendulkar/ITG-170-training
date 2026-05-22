# Create a function greet() that prints a welcome message.
def greet():
    print("welcome")
greet()



# Create a function that accepts two numbers and returns the larger number.
def twonum(a,b):
    return a if a>b else b
print(twonum(int(input()),int(input())))



# Write a function that calculates the area of a rectangle.
def area(l,w):
    return l*w
print(area(int(input()),int(input())))



# Create a function that accepts any number of numbers and returns their sum.
def ar(*nums):
    return sum(nums)
print(ar(1,20,56))

# Add a doc string to any one function explaining what it does.
def ar(*nums):
    '''
     this fn accepts any num of 
     numbers and 
     returns value'''
    return sum(nums)
print(ar(1,20,56))




# Write a function that returns the square of a number.
def square(n):
    return n**2
print(square(2))



# Write a function that checks if a number is even.
def even(n):
    return "even" if n%2==0 else "odd"
print(even(int(input())))




# Create a function that greets a user using their name (parameter).
def greet(name):
    return f"Welcome {name}"
print(greet(input()))



# Create a function that finds the average of 3 numbers.
def avg(n1,n2,n3):
    return (n1+n2+n3)//3
print(avg(1,3,2))


# Add proper doc string to one function
def avg(n1,n2,n3):
    ''' calculate the avg of 3 nums
        Params: n1,n2,n3
        return val: 
        int or float
        avg of three nums
       '''
    return (n1+n2+n3)/3
print(avg(1,3,2))



