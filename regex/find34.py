import re

text = "Python is great and coding is fun"

str1=re.findall(r'\b\w{3,5}\b',text)

print(str1)