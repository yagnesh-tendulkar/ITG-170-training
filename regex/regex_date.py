import re

url = "https://example.com/2026/05/17/sample"

result = re.findall(r'(\d{4})/(\d{2})/(\d{2})',url)
print(result)