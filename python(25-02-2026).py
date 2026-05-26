import math
# n=6
# c=1
# for i in range(2,n+1):
#     if n%i ==0:
#         c+=1
# if c >2:
#     print("not a prime number")
# else:
#     print("its prime number")

# Given [1,2,3,4,5,6], create new list of squares of even numbers using comprehension

# list1 =[1,2,3,4,5,6]
# print([i**2 for i in list1 if i%2 == 0])

# Count frequency of each character in a string using dictionary
# s = "roshini priya"
# freq={}
# for char in s:
#     if char in freq:
#         freq[char] += 1
#     else:
#         freq[char] =1
# print(freq)


# print(f"Value:{.2f}".format(3.14159))
print(f"Value:{3.14159:.2f}")
print("hello ".strip())
print("heelo".replace("h",'j'))
# if elif is a choice but nested if is process or flow
# print(list(range(2,10,2)))
# the filter function is used to filter the elements of a sequence based on a function that tests each element in the sequence to be true or not.
print(list(filter(lambda x: x>2,[1,2,3,4,5])))
# here the filter function returns as iterator which satisfies the condition and that was type casted to list beacuse filter function returns an iterator and we want to the see the list.
# the lambda function is  used to create an anonymous function that can be used as an argument to the filter function. in this case the lambda function takes one argument x and returns true if x is greater than 2 and false otherwise.
# the default values of filter are filter(function, iterable)
from collections import Counter,UserDict,deque
# from collections import deque,Conuter,UserDict
# from collections import UserList
# class Mylist(UserList):
#     def append(self,item):
#         super().append(item.upper())
# # here userlist is a class which we are inheriting from the userlist class and super() is a a functions which is used to call the mehtod in the parent class
# mylist = Mylist()
# mylist.append("hello")
# print(mylist)
from collections import UserList
class Mylist(UserList):
    def append(self,item):
        super().append(item.upper())

m = Mylist()
m.append('helloworld')
m.append("tere meri")
print(m)

# iterators
n =[1,2,3,4]
it =iter(n)
print(next(it))
print(next(it))
print(next(it))

# generators 
# def count_n(n):
#     i=0
#     while i<=n:
#         yield i
#         i += 1
# for v in count_n(5):
#     print(v)


def count_n(n):
    i=1
    while i<=n:
        yield i +1
        yield "hai"
        i *=2
for v in count_n(5):
    print(v)
# any function is taking [] as an argument because it is 
# if any doesnt take list as an argument 
print(any(["true","false"]))
print(all(['',"true"]))
# with open("list_comprehension.txt",'r') as f:
#     print(f.read())

def timer(func):
    def wrapper():
        import time
        s = time.time()
        func()
        e = time.time()-s
    return wrapper
@timer
def slow_timer():
    print("slow timer")
import re
print(re.findall(r'[\d+]', "123abc"))
