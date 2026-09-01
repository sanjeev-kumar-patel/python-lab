# fh = open("MySelf.txt", 'r')
# content = fh.read(50)
# print(content)
# fh.close()

# 1) a)
# fh = open("python.txt",'w')

# fh.writelines("Python is a high level programming language.\n")
# fh.writelines("CyberSceurity use python as their language.\n")
# fh.writelines("We can also make website through python using framework like flask, streamlit.\n")
# fh.writelines("This language is used to train the machine learning model.\n")
# fh.writelines("It is a simple language.\n")

# fh.close()

# fh = open("python.txt",'r')

# content = fh.read()

# print(content, "\n")
# # print("\n")

# fh.seek(0)

# content1 = fh.readlines()

# print(content1)
# # print("\n")

# fh.seek(0)

# for line in content:
#     content2 = fh.readline()
#     print(content2)
# fh.seek(0)
# content3 = fh.read(30)
# print(content3)
# fh.close()




# 1. c)
fh = open("python.txt", "w")

fh.writelines("Python is a high level programming language.\n")
fh.writelines("Python is easy to learn and simple to understand.\n")
fh.writelines("Python is widely used in software development.\n")
fh.writelines("Python is used to develop websites and applications.\n")
fh.writelines("Python is also used in machine learning and AI.\n")

fh.close()

fh = open("python.txt", "r")

content = fh.read()
print(content)

fh.seek(0)

print("\nUsing readline():")
print(fh.readline())

fh.seek(0)

print("Using readlines():")
print(fh.readlines())

fh.seek(0)

print("\nFirst 30 characters:")
print(fh.read(30))

fh.close()

fh = open("python.txt", "a")

fh.writelines("\nPython has several data types such as integer, float, string, list, tuple, set and dictionary.\n")
fh.writelines("These data types are used to store different kinds of values in Python.\n")

fh.close()

fh = open("python.txt", "w+")

fh.seek(10)

print("\nReading from 10th character:")
content = fh.read()
print(content)

fh.close()


