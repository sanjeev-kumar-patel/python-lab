students = {}

for i in range(9):
    roll = int(input("Enter roll no: "))
    marks = int(input("Enter marks: "))
    students[roll] = marks

if len(students) == 9:
    roll = int(input("Enter roll no of 10th student: "))
    marks = int(input("Enter marks: "))
    students[roll] = marks

print("Keys:", students.keys())
print("Values:", students.values())

students[2] = int(input("Enter updated marks for roll no 2: "))

print(students)