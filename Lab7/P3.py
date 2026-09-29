# P3: Demonstrate basic regular expressions by using search(), match(), split(), findall(),
# group()

import re

text = "My phone number is 9876543210 and my age is 20."

# search()
result = re.search(r"\d+", text)
print("search():", result.group())

# match()
result = re.match(r"My", text)
print("match():", result.group())

# split()
result = re.split(r"\s+", text)
print("split():", result)

# findall()
result = re.findall(r"\d+", text)
print("findall():", result)

# group()
result = re.search(r"phone number is (\d+)", text)
print("group():", result.group(1))