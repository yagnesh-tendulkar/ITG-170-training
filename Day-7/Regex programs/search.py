import re

text = "Hello world"

pattern = r"^Hello"

if re.search(pattern, text):
    print("String starts with Hello")
else:
    print("No match")