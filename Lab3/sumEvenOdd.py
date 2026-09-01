# 2. Write a Python program that calculates the sum of even and odd numbers 
# separately within a given range. Implement a function that takes the range 
# as input and returns the sum of even and odd numbers within that range.

lowerLimit = int(input("Enter the lower limit: ")) 
upperLimit = int(input("Enter the upper limit: "))
sumE = 0
sumO = 0
for i in range(lowerLimit,upperLimit+1):
    if(i%2 == 0):
        sumE = sumE + i;
    else :
        sumO = sumO + i;
print(f"Sum of Even Number from [{lowerLimit},{upperLimit}] = {sumE}")
print(f"Sum of Odd Number from [{lowerLimit},{upperLimit}] = {sumO}")