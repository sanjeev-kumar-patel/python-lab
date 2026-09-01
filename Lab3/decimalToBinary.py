# 5.	Write a Python program that takes a floating-point value as input from the user and outputs the binary equivalent of that number (up to 10 digits). 
# For example: 
# Input: 		2.2
# Output:	10.00110011000

num = float(input("Enter a floating-point number: "))

# Integer part
integer_part = int(num)


integer_binary = bin(integer_part)[2:]

fraction = num - integer_part
fraction_binary = ""
for i in range(10):
    fraction = fraction * 2

    if fraction >= 1:
        fraction_binary = fraction_binary + "1"
        fraction = fraction - 1
    else:
        fraction_binary = fraction_binary + "0"

print("Binary equivalent:", integer_binary + "." + fraction_binary)
