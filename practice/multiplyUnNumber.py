def multiplier(n):
    return lambda x: x * n

double = multiplier(2)
triple = multiplier(3)
quadruple = multiplier(4)
quintuple = multiplier(5)

print("Double:", double(15))
print("Triple:", triple(15))
print("Quadruple:", quadruple(15))
print("Quintuple:", quintuple(15))