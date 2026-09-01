# 1.	Write a program to find factorial of a number using Recursion.
def fact(n) :
    if(n == 0 or n == 1):
        return n;
    return n*fact(n-1)
n = int(input("Enter Number: "))
print(f"{n}! = {fact(n)}")