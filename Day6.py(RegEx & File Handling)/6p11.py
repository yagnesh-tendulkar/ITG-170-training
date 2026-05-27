def multiplier(n):
    return lambda x: x * n
double = multiplier(2)
triple = multiplier(3)
quadruple = multiplier(4)
quintuple = multiplier(5)
print(double(15))
print(triple(15))
print(quadruple(15))
print(quintuple(15))