import re
text = "Python,Java;C++ SQL"
result = re.split(r'[,; ]+', text)
print(result)