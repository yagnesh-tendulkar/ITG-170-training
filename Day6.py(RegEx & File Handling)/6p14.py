import re
string = "Python code Java SQL HTML CSS"
result = re.findall(r'\b\w{3,5}\b', string)
print(result)