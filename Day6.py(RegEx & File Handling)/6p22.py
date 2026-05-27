import re
text = ["a", "ab", "abb", "ac"]
for i in text:
    if re.fullmatch(r'ab?', i):
        print(i)