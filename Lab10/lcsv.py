# Create Comma Separate Files (CSV), Load CSV files into internal Data Structure

import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Roll_No", "Name", "Marks"])
    writer.writerow([1, "Aman", 85])
    writer.writerow([2, "Riya", 90])
    writer.writerow([3, "Rahul", 78])

students = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)

print("Student Records:")

for student in students:
    print(student)
    
