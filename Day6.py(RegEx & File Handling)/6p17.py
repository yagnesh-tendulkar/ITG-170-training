import re
text = "Hello@123#Python!!"
result = re.sub(r'[^A-Za-z0-9]', '', text)
print(result)