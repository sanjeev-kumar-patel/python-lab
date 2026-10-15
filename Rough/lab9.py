import sqlite3

conn = sqlite3.connect("college.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Students")
cur.execute("DROP TABLE IF EXISTS Departments")

cur.execute("""
CREATE TABLE Students (
    student_id INTEGER PRIMARY KEY,
    student_name TEXT,
    department_id INTEGER
)
""")

cur.execute("""
CREATE TABLE Departments (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT
)
""")

cur.executemany("INSERT INTO Students VALUES (?, ?, ?)", [
    (1, "Aman", 101), (2, "Riya", 102),
    (3, "Rahul", 103), (4, "Priya", None)
])

cur.executemany("INSERT INTO Departments VALUES (?, ?)", [
    (101, "CSE"), (102, "ECE"), (104, "Mechanical")
])

queries = {
    "INNER JOIN": """
        SELECT student_id, student_name, department_name
        FROM Students INNER JOIN Departments
        ON Students.department_id = Departments.department_id
    """,
    "LEFT JOIN": """
        SELECT student_id, student_name, department_name
        FROM Students LEFT JOIN Departments
        ON Students.department_id = Departments.department_id
    """,
    "RIGHT JOIN": """
        SELECT student_id, student_name, department_name
        FROM Students RIGHT JOIN Departments
        ON Students.department_id = Departments.department_id
    """,
    "FULL OUTER JOIN": """
        SELECT student_id, student_name, department_name
        FROM Students FULL OUTER JOIN Departments
        ON Students.department_id = Departments.department_id
    """
}

for name, query in queries.items():
    print(f"\n{name}")
    cur.execute(query)
    print("Student ID | Name | Department")
    for row in cur.fetchall():
        print(row)

conn.close()

