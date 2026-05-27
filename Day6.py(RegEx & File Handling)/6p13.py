cities = [("Delhi", 3000000), ("Vizag", 1500000), ("Mumbai", 5000000), ("Chennai", 2000000)]
result = list(filter(lambda x: x[1] > 2000000, cities))
print(result)