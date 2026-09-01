n = float(input("Enter the marks you got out of 100. "))
if n <= 100 and n > 90 :
    print("Grade A+ ")
elif n <= 90 and n > 80 :
    print("Grade A ")
elif n <= 80 and n > 70:
    print("Grade B+")
elif n <= 70 and n > 60:
    print("Grade B ")
elif n <= 60 and n > 50: 
    print("Grade C+")
elif n <= 50 and n > 40:
    print("Grade C")
else :
    print("Fail")