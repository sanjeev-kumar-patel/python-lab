# 4.	Write a program to Convert a binary number taken as user input into its decimal equivalent.
# User Input: 	101010
# Output:	42

bit = input("Enter a binary number: ")

decimal = 0
power = 0

for digit in bit[::-1]:
    decimal = decimal + int(digit) * (2 ** power)
    power = power + 1

print(f"{bit} =>  {decimal}")
