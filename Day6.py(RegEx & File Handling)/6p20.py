import re
text = "Python Program"
result = re.sub(r'\s', '_', text)
print(result)
text2 = "Python_Program"
result2 = re.sub(r'_', ' ', text2)
print(result2)