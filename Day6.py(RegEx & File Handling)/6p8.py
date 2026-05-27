lst = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
result = list(filter(lambda x: x is not None, lst))
print(result)