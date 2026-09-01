file = open("example.txt", "w")

file.write("Hello, Python!")
file.close()

file = open("example.txt", "r")

content = file.read()
print(content)

file.close()

file = open("example.txt", "a")

file.write("\nWelcome to Python.")

file.close()