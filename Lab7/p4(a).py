# P4: Demonstrate advanced regular expressions for validationp

import re

# a) Validate Mobile Number
phone = input("Enter mobile number: ")

if re.fullmatch(r"^[6-9][0-9]{9}$", phone):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")


# b) Validate Landline Number
landline = input("Enter landline number: ")

if re.fullmatch(r"^[0-9]{2,4}-[0-9]{6,8}$", landline):
    print("Valid Landline Number")
else:
    print("Invalid Landline Number")


# c) Validate Email ID
email = input("Enter email ID: ")

if re.fullmatch(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", email):
    print("Valid Email ID")
else:
    print("Invalid Email ID")


# d) Validate Password
password = input("Enter password: ")

if (len(password) >= 8 and
    re.search(r"[A-Z]", password) and
    re.search(r"[a-z]", password) and
    re.search(r"[0-9]", password) and
    re.search(r"[^A-Za-z0-9]", password)):

    print("Strong Password")
else:
    print("Weak Password")