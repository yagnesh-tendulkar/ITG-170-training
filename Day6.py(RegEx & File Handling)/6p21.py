import re
text = ["a", "ab", "abbb", "ac"]
for i in text:
    if re.fullmatch(r'ab*', i):
        print(i)