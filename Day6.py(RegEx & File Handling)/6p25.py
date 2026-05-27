import re
url = "https://www.example.com/2026/05/22/article"
result = re.search(r'(\d{4})/(\d{2})/(\d{2})', url)
print("Year:", result.group(1))
print("Month:", result.group(2))
print("Date:", result.group(3))