# Write script to work like a SQL Inner Join 
# for an internal Data Structure made in earlier exercise

import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Student_ID", "Name", "Department_ID"])
    writer.writerow([1, "Aman", 101])
    writer.writerow([2, "Riya", 102])
    writer.writerow([3, "Rahul", 101])
    writer.writerow([4, "Neha", 103])

with open("departments.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Department_ID", "Department_Name"])
    writer.writerow([101, "CSE"])
    writer.writerow([102, "ECE"])
    writer.writerow([104, "Mechanical"])

with open("students.csv", "r") as file:
    students = list(csv.DictReader(file))

with open("departments.csv", "r") as file:
    departments = list(csv.DictReader(file))

department_map = {
    department["Department_ID"]: department["Department_Name"]
    for department in departments
}

print("Student_ID\tName\tDepartment")

for student in students:
    dept_id = student["Department_ID"]

    if dept_id in department_map:
        print(
            student["Student_ID"],
            student["Name"],
            department_map[dept_id],
            sep="\t"
        )

