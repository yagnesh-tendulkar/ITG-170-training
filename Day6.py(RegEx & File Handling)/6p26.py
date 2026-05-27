import re
text = "abc123xyz45"
for match in re.finditer(r'\d+', text):
    print(match.group(), "Position:", match.start())