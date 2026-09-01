# P8: Write a program that swaps the values of two variables using a
# temporary variable.

n1 = float(input("Enter the First Number: "))
n2 = float(input("Enter the Second Number: "))
print("Initial First Number: ", n1)
print("Initial Second Number: ", n2)
temp = n1
n1 = n2
n2 = temp
print("Final First Number: ", n1)
print("Final Second Number: ", n2)