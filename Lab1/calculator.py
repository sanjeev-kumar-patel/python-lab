n1 = float(input("Enter the first Number: "))
n2 = float(input("Enter the first Number: "))
op = input("Enter the operation: ")
if op == '+' :
    print(n1," + " ,n2, " = ", n1 + n2)
elif op == '-' :
    print(n1, " - ", n2, " = ", n1 - n2)
elif op == '*' :
    print(n1, " * ", n2, " = ", n1 * n2)
elif op == '/' :
    if n2 == 0 :
        print("Denominator can't be zero. ")
    else :
        print(n1, "\\", "n2", " = ", n1/n2)
else : 
    print("Invalid Operation.")
    