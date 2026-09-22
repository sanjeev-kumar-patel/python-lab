#Regular epression is a pattern used to search,match,extract, or validate text
import re
text = "Python is fun. We are learning Python"
# r = re.search("Python",text)  # Search the words in the line
# r = re.match("Python",text)
# r = re.match("We",text)  # Searching the begining of the line
# if r:
#     print("Match found")
# else:
#     print("No match found")


# r = re.sub("Python","Java",text)
# print(r)

# r = re.findall("Python",text)
# print(r)

# text1 = "Python,   is; fun. We are, learning Python"
# r = re.split("[,;.]",text1)
# print(r)
# r = re.split("[,;.\s]",text1)
# print(r)
# r = re.split("[,;.\s]+",text1)
# print(r)
# r = re.split(r"[,;.\s]+",text1)
# print(r)

#MetaCharacters
# . (Dot) means any character r'a.b'  matches  abb avb abb agb  (first letter is a 
# and something and last letter is b)
# ^ beginning  r'^Hello'  Hello World
# # $ end  r'World$'  Hello World
# *  0 or more     r'ab*'   matches a ab abb 
# + 1 or more   r'ab+'  matches ab abb abbb

# ? 0 or 1   r'colou?r'   matches  color colour

# [a-z]  r'[a-z]'   
# [A-Z]  
# [0-9]
# \d     digits  r'\d'   e.g  \d{2,4} character of length 2 to 4 ; \d{3} character of length 3
# \D     not digits
# \w    wprd characters
# \s   whitespaces
# \S  no white spaces
   
text = "My age is 123, my r_no is 23"
r = re.findall(r'\d',text)
print(r)
r = re.findall(r'\d+',text)
print(r)
r = re.findall(r'\d{2,3}+',text)
print(r)
r = re.findall(r'\D',text)
print(r)
r = re.findall(r'\w+',text)
print(r)
r = re.findall(r'\W+',text)
print(r)
r = re.findall(r'\w',text)
print(r)
r = re.findall(r'a.b',text)
print(r)
r = re.findall(r'a.e',text)
print(r)
r = re.findall(r'm+',text)
print(r)
r = re.findall(r'ag+',text)
print(r)
r = re.findall(r'ab*',text)
print(r)
r = re.findall(r'[a-z]',text)
print(r)
r = re.findall(r'[A-Z]',text)
print(r)
r = re.findall(r'[A-z]',text)
print(r)


number = "2312312321 2131 3213213212 4353656767 432 321 432 43234323 dfas fdjasljfad ljfdlajf ldskajf ajkfjal falfj alk"
r = re.findall(r'\d{10}',number)
print(r)
