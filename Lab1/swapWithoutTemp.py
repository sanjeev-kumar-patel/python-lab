# P9: Write a program that swaps the values of two variables without
# using a temporary variable.

a = int(input("First Number: "))
b = int(input("Second Number: "))
print("a = ", a)
print("b = ", b)
a = a+b
b = a-b
a = a-b
print("a = ", a)
print("b = ", b)
