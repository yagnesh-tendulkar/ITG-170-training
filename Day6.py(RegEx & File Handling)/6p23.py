import re
text = ["a123b", "axxxb", "ab", "ac"]
for i in text:
    if re.fullmatch(r'a.*b', i):
        print(i)