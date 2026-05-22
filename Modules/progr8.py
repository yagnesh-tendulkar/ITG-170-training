import global_var as g
def deposit(amount):
    g.balanace += amount
    return g.balanace
def withdraw(amount):
    g.balanace -= amount
    return g.balanace
print(deposit(2000))
print(withdraw(4000))
