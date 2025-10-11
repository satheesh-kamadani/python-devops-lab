import re

text = "apple,banana,orage,grape"
pattern = r","

split_result = re.split(pattern, text)
print("Split results: ", split_result )