import re

text = "Python is awesome"
pattern = r"Python"

match = re.match(pattern, text)
if match:
    print("Match found: ", match.group())
else:
    print("Match not found")