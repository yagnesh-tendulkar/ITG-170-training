import re
text = ["amazing", "zoo", "buzz", "apple"]
for i in text:
    if re.search(r'\Bz\B', i):
        print(i)