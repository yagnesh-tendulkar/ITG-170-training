# zero diviosn error
# try:
#     result  = 23/0
# except ZeroDivisionError:
#     print("cannot divide by zero")
# Value error
# try: 
#     a = int(input("enter your value"))
#     print(a)
# except ValueError:
#     print("The input accepts only numneric value")
# type error 
# try: 
#     a = int(input("enter your value"))
    
#     print("the input value is ",a)
# except ValueError:
#     print("The input accepts only numeric value")
#     try:
#         c  = int(input("try to give a int type"))
        
#         print("the typed input is",c)
#     except ValueError:
#         print("the type is not right")
# ================================
# try:
#     z = "5" +5
# except TypeError:
#     print("the type is different")
#     print(5 + 5)
# ==========
class MyObject:
    a = 10
    def some_menth(self):
        print("the main method of this class")
obj = MyObject()
try:
    obj.some_meth()
except AttributeError:
    print("Attribute not found")



