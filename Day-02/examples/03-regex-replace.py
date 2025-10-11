import re

text = "Python is static typed programming language"
pattern = r"static"

replacement = "dynamically"

new_text = re.sub(pattern, replacement, text)
print("Modified text: ", new_text)