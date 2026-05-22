# try:
#     x = 1
# except ZeroDivisionError:
#     print("error handled")
# we have asertion error also
# f = False
# try: 
#     assert f == True, "yes its true"
#     print("assertion is true")
# except AssertionError:
#     print("the assertion is not correct")
    # assertion is a debugging check using the key work assert. 
    # if the asserted value is correct the program continues if not it will raise an assertion error exception from the except block.

# try:
#     x = 10/0
# except ZeroDivisionError:
#     print("error handled")
# finally:
#     print("completed")
# finally no matter what it will print the block of code if (error or not)
# try:
#     i = int(input())
#     try:
#         k = i/0
#     except ZeroDivisionError:
#         print("error modified")
# except TypeError:
#     print("the type is not correct")

# ==========================
# try:
#     i = input()
#     try:
#         k = i/0
#     except ZeroDivisionError:
#         print("error modified")
# except TypeError:
#     print("the type is not correct")
# ===================== these are the try with multiple try blocks i mean nested try -except
# raising an exception:
# x =18
# if x < 19:
#     raise ValueError("the value is incorrect")
# ====================== custom exceptions - creating exception class and raising the exception and handling the exception
# class AgeErro(Exception):
#     pass
# try:
#     age = int(input("Enter your age:"))
#     if age < 18:
#         raise AgeErro("you must be 18+")
#     print("access granted")
# except AgeErro as e:
#     print("custom exception:",e)
# ======================
def func():
    return 10 / 0

func()  # error propagates
