# l =[0,1,2,3,4]
# print(all(i for i in l if i > 0))
# # all() means that all the elements in the list should satisfy the condition i >= 0 for the result to be True. Since all elements in the list are greater than or equal to 0, the output will be False.

# def fun():
#     try:
#         return 1
#     finally:
#         return 2
# print(fun())

# l = [i for i in range(3)]
# g = (i for i in range(3))
# # g is generator type but why not set as () represents set what can be the reason for this 
# #  
# print(type(l),type(g))
# s ={i for i in range(3)}
# print()
# print(type(s))
# def gen():
#     for i in range(3):
#         yield i
# g = gen()
# print(list(g))
# # i want the use of using generators and list(g) means it works same as for loop but its more memory efficinet because it generates 

# g= gen()
# print(list(g))
# # list(g) 

# g = [1,2,3,4]
# g =3
# print(g)
# print(list(g))
# what is the difference list(g) and g
# list(g) creates a new list that contains and i can know the address of the list created by list(g) and the original list g with the syntax  id () function
# print(id(g))
# print(id(list(g)))
# from the sbove code we can see the address of each are different which means that list(g) creates a new list in the memory and they are stored i diffeent memory locations.

# def fun(a,b=[]):
#     b.append(a)
#     return b
# print(fun(1))
# import time
# for i in range(5,0,-1):
#     print(i, end=" ",flush = True)
#     time.sleep(1)
# print("blast off")
# flush is used in real time updates and to create a countdown effect by immediately printing the elements to the console without waiting  for the buffer to fill up or for a new line charachter to be encountered.
# buffer means 
# list1 = [1,2,3,45]
# list2 =[1,2,3,4,5,6]
# list2.extend(list1)
# print("extend:", list2)
# list1.insert(3,23)
# print("insert:", list1)
# print()
# list2.pop(3)
# print("pop:", list2)
# list2.remove(5)
# print("remove:",list2)
# print(type(True))

# dic1 = {"1":"Roshini","2": "harika","3": "Sneha"}
# tuple_keys = tuple(dic1.values())
# print(tuple_keys)
# print()
# print(dic1)
# print()
# for k,v in dic1.items():
#     print(f"{k} :{v}")

# x=10
# print(~(x))
# print(x << 4)
# print(x >> 4)
# a=-12
# print(a >> 1)
# if True:
#   print("true")
#    print("fasle")
# unexpected indentation 
# 1. .lower() and .upper() and .strip() and .replace(old,new) and .join(iterble) means replace (old,neww) means haing 

# def add(*args):
#     return sum(args)
# print(add(1,2,3,4))
# print(add(1,2,3,4,5))
# def add(a,b,c=0):
#     return a + b +c
# print(add(12,23))
# print(add(1,2,3))

import re
# text ="apple;;;;mana,banana;cherryidouble"
# print(re.split("[,;i]", text))
# print(re.split("[;]", text)) 
# print(re.split("[,ein]",text))
# print(re.split("[,ein]",text))
# print(text[5:11])
# print(re.findall(r"^ hello","say hello world"))
# s ="cat"
# print(re.findall(r"t$",s))
# print(re.findall(r'a',s))
# print(re.findall(r"^apple","applepine"))
# print(re.findall(r'^\w+$',s))
# print(re.findall(r'[^0-9]','A1'))
# # ex
# print(re.findall(r'^ghost$','ghostbuster'))

# ++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++
# Given this text:
# text = "I have 10 apples, 25 oranges, and 3 bananas"

# # Use findall() to extract all numbers
# # Expected output: ['10', '25', '3']
# print(re.findall(r'\d+',text))
# Given this text:
# text = "Hello world! Python is awesome. Regex is fun."

# Extract all words (letters only, no punctuation)
# Expected output: 
# text = "Hello world! Python is awesome. Regex is fun."
# r = re.findall(r'[A-Za-z]',text)
# print(r)

# ++++++++++++++++++++++++++++++++++

# Given this text:
# text = "Contact us at support@example.com or sales@company.co.uk. Invalid: user@.com"
# print(re.findall(r'[\w.]+@[\w.]+',text))

# # Given this text:
# text = "Call me at 123-456-7890 or 987-654-3210. Also 555-123-4567"
# print(re.findall(r'[\d-]+',text))
# # Extract all phone numbers in format XXX-XXX-XXXX
# Expected output: ['123-456-7890', '987-654-3210', '555-123-4567']

# +++++++++++++++++++++++++
# Given this text:
# text = "Loving #Python and #Regex! #100DaysOfCode is great. #no-spaces-allowed"
# print(re.findall(r'#\w+',text))
# what is the difference between r'[#\w+]' and r#\w+ in regex pattern is 
# Extract all hashtags (starts with #, followed by letters/numbers/underscore)
# Expected output: ['#Python', '#Regex', '#100DaysOfCode']
# ++++++++++++++++++++++
# explain the above regex pattern r'[\w\.-]+@[\w\.-]+': first 
# Extract all valid email addresses
# Expected output: ['support@example.com', 'sales@company.co.uk']
# ++++++++++++++++++++++++++++
# # Given this text:
# text = "Dates: 2024-01-15, 15/01/2024, Jan 15 2024, and 2024.12.25"
# print(re.findall(r'\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}|\w{3} \d{2} \d{4}|\d{4}\.\d{2}\.\d{2}',text))
# Extract all dates in ANY of these formats:
# YYYY-MM-DD, DD/MM/YYYY, MMM DD YYYY, YYYY.MM.DD
# Expected output: ['2024-01-15', '15/01/2024', 'Jan 15 2024', '2024.12.25']
# +++++++++++++++++++++++++++++++
# Given this text:
# text = "Visit https://python.org or http://example.com/page. Also ftp://files.com"
# print(re.findall(r'http?://\w+\.\w+|ftp://\w+\.\w+',text))
# Extract all URLs (http://, https://, ftp://)
# Expected output: ['https://python.org', 'http://example.com/page', 'ftp://files.com']
# +++++++++++++++++++++++++++++++

# how to use this ^ in regex means 
# r means 
# print(re.findall(r"a *","aa a aaa aaaaa"))
# print(re.match(r"\d","04roshini priyanka"))

# print(re.search(r"\d","roshini 04"))
# text = "my number is 123a"
# print(re.sub(r'\d','*',text))
# working with emails usind findall 
# text ="text@gmail.com"
# pattern = r'\w+@\w+.\w+'
# print(re.findall(pattern,text))
# how should i know the pattern r'\w+@\w+\.\w+' will work 

# @decorator(greet):
# def wrapper(:
#             )
# @decorator(greet):

#     def wrapper():
#         print("hello")
#     greet()
#     def wrapper():
#         print("hello")
# greet()
# from curses import wrapper


# @decorator
# def decorator(func):
#     def wrapper():
#         print("before")
#     func()
#     def wrapper():
#         print("after")
#     return wrapper
# decorator(greet())

# def decorator(func):
#     def wrapper():
#         print("before")
#         func()
#         print("after")
#     return wrapper
# @decorator
# def greet():
#     print("hai")
# greet()
#  decorating a function means adding extra function to the actual code without modifying the exisiting code 
# mat = [[1,2],[3,4]]
# # flat = [j for i in mat for j in i]
# flat = [ j for i in mat for j in i if j%2]
# print(flat)
# Create a dictionary comprehension to store squares of numbers from 1–5.
# my_dict = {num: num * num for num in range(1,6)}
# print(my_dict)

# n =[i for i in range(1,21) if i%2]
# print(n)
# try:
#     print("Start")
#     raise ValueError
#     print("End")
# except ValueError:
#     print("Error")
# finally:
#     print("Done")
     
# class MyError(Exception):
#     pass

# try:
#     raise MyError("Test")
# except MyError:
#     print("Handled")
# class MyBug(Exception):
#     pass
# age =-5
# try:
#     if age < 0:
#         raise MyBug("The age cannot be negative")
# except MyBug as b:
#     print(b)
    





# fibanocci
n=5
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b= b,a+b
a,b=0,1
print()
while(n>0):
    print(a,end=" ")
    a,b=b,a+b
    n-=1