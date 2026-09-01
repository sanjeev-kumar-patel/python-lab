# IOError,NameError,TypeError,KeyError,ValueError,IndexError,ImportError,FileExistsError,FileNotFoundError,ZeroDivisionError


# try:
#     fh = open("python.txt", "r")
    
#     content = fh.read()

# except FileNotFoundError:
#     print("File not found.")

# except PermissionError:
#     print("Permission denied.")

# except Exception as e:
#     print("An error occurred:", e)

# else:
#     print(content)
#     print("File read successfully.")
#     fh.close()

# finally:
#     print("File operation completed.")






# try:
#     fh = open("python.txt", "r")
    
#     content = fh.read()
    
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
    
#     result = a / b
    
#     my_list = [10, 20, 30]
#     print(my_list[5])
    
#     my_dict = {"name": "Sanju"}
#     print(my_dict["age"])

# except IOError:
#     print("IOError: Input/output error.")

# except NameError:
#     print("NameError: Variable is not defined.")

# except TypeError:
#     print("TypeError: Invalid data type.")

# except KeyError:
#     print("KeyError: Key does not exist.")

# except ValueError:
#     print("ValueError: Invalid value entered.")

# except IndexError:
#     print("IndexError: Index is out of range.")

# except ImportError:
#     print("ImportError: Module could not be imported.")

# except FileExistsError:
#     print("FileExistsError: File already exists.")

# except FileNotFoundError:
#     print("FileNotFoundError: File does not exist.")

# except ZeroDivisionError:
#     print("ZeroDivisionError: Cannot divide by zero.")

# else:
#     print("File read successfully.")
#     print(content)
#     fh.close()

# finally:
#     print("Exception handling completed.")



# IOError

try:
    fh = open("pyto.txt", "r")
    print(fh.read())
    fh.close()
except IOError as ioe:
    print("IOError : " ,ioe)
else:
    print("File operation successful.")


# NameError

try:
    print(name)
except NameError as ne:
    print("NameError" , ne)
else:
    print("Variable exists.")


# TypeError

try:
    a = 10
    b = "20"
    result = a + b
except TypeError as te:
    print("TypeError: " ,te)
else:
    print(f"Result is {result}")


# KeyError

try:
    student = {"name": "Sanjeev", "age": 20}
    print(student["course"])
except KeyError as ke:
    print("KeyError : " ,ke)
else:
    print("Key exists.")


# ValueError

try:
    n = int(input("Enter a number: "))
    print(f"Number is {n}")
except ValueError as ve:
    print("Value : ",ve)
else:
    print("Valid number entered.")


# IndexError

try:
    l = [1, 2, 3]
    print(l[4])
except IndexError as ie:
    print("IndexError : " ,ie)
else:
    print("Index exists.")


# ImportError

try:
    from math import abc
except ImportError as ime:
    print("ImpoerError : " ,ime)
else:
    print("Import successful.")


# FileExistsError

try:
    fh = open("python.txt", "x")
    fh.close()
except FileExistsError as fee:
    print("FileExistsError : " ,fee)
else:
    print("File created successfully.")


# FileNotFoundError

try:
    fh = open("sanjeev.txt", "r")
    print(fh.read())
    fh.close()
except FileNotFoundError as fnfe:
    print("FileNotFoundError : ",fnfe)
else:
    print("File exists.")


# ZeroDivisionError

try:
    a = int(input("Enter n1: "))
    b = int(input("Enter n2: "))
    divide = a / b
except ZeroDivisionError as zd:
    print("ZeroDivisionError : ",zd)
else:
    print(f"Division is {divide}")