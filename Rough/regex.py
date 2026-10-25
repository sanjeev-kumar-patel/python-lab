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

text = "7882345123"
x = re.search(r"(\d{3})(\d{4})(\d{3})",text)

if x:
    print(x.group(1))
    print(x.group(2))
    print(x.group(3))
    
text = "9906805337"
x = re.search(r"(\d{6})(\d{4})",text)
if x:
    print(x.group(1))
    print(x.group(2))

## Validation
p_no = input("Enter phone number: ")
pattern=r"^[6-9]\d{9}$"
if re.fullmatch(pattern,p_no):
    print("Valid No.")
else:
    print("Invalid")

## Validation of Email Id

email = input("Enter the email: ").strip()

pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|in)$"

if re.fullmatch(pattern, email):
    print("Valid")
else:
    print("Invalid")
    
## Password validate atleast 8 characters, one upppercase, one lowercase


pwd = input("Enter Password: ")

pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"

if re.fullmatch(pattern, pwd):
    print("Strong")
else:
    print("Weak")
    
if (len(pwd) >= 8 and re.search(r"[A-Z]",pwd) and re.search(r"[a-z]",pwd) and re.search(r"[0-9]",pwd)):
    print("Valid")
else:
    print("Invalid")
    