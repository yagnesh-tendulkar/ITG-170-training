import re
text = "Visit https://www.google.com and http://example.com"
result = re.findall(r'https?://\S+', text)
print(result)