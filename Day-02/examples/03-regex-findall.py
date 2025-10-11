import re

text = "Python is an awesome programming language"
pattern = r"awesome"

search = re.search(pattern, text)
if search:
    print("Pattern found: ", search.group())
else:
    print("Pattern not found")