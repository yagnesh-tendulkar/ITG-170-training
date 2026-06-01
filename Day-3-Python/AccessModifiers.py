class MyClass:
    public_variable='public_variable'
    _protected_variable='_protected_variable'
    __private_variable='__private_variable'

obj= MyClass()
print(obj.public_variable)
print(obj._protected_variable)
print(obj._MyClass__private_variable)