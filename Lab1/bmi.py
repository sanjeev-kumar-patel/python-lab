# P7: Write a program that calculates the BMI based on user's weight
# and height.

w = float(input("Enter Weight(in Kg): "))
h = float(input("Enter height(in m): "))
bmi = w/(h*h)
print(f"BMI = {bmi}")