'''Create a student database using Python and MySQL. 
Insert 5 students using executemany(). 
Display all students, display CSE students, display students having marks greater than 85, 
update marks of a student, and delete a student.'''

import sqlite3

# Connect to database
db = sqlite3.connect("student.db")
cur = db.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    branch TEXT,
    marks INTEGER
)
""")

# Insert 5 students using executemany()
students = [
    (1, "Rahul", "CSE", 90),
    (2, "Priya", "ECE", 82),
    (3, "Aman", "CSE", 88),
    (4, "Neha", "ME", 75),
    (5, "Riya", "CSE", 92)
]

cur.executemany(
    "INSERT INTO students VALUES (?, ?, ?, ?)",
    students
)
db.commit()

# Display all students
print("\nAll Students:")
cur.execute("SELECT * FROM students")
for row in cur.fetchall():
    print(row)

# Display CSE students
print("\nCSE Students:")
cur.execute("SELECT * FROM students WHERE branch = ?", ("CSE",))
for row in cur.fetchall():
    print(row)

# Display students with marks > 85
print("\nStudents with marks > 85:")
cur.execute("SELECT * FROM students WHERE marks > ?", (85,))
for row in cur.fetchall():
    print(row)

# Update marks
student_id = int(input("\nEnter student ID: "))
new_marks = int(input("Enter new marks: "))

cur.execute(
    "UPDATE students SET marks = ? WHERE id = ?",
    (new_marks, student_id)
)
db.commit()

print("Marks updated successfully.")

# Delete a student
student_id = int(input("\nEnter student ID to delete: "))

cur.execute(
    "DELETE FROM students WHERE id = ?",
    (student_id,)
)
db.commit()

print("Student deleted successfully.")

db.close()

db = sqlite3.connect("student.db")
cur = db.cursor()

print("\nCSE Students:")
cur.execute("SELECT * FROM students WHERE branch = ?", ("CSE",))
for row in cur.fetchall():
    print(row)
db.close()