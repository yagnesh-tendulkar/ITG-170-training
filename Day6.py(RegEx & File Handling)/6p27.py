import re
text = "Python, Java. SQL   HTML"
result = re.sub(r'[ ,\.]+', ':', text)
print(result)