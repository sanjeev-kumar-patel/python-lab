import sqlite3
conn = sqlite3.connect("college.db")
cur = conn.cursor()

cur.execute("Drop table if exists Students")
cur.execute("Drop table if exists Departments")

cur.execute("""Create table Students (student_id INTEGER PRIMARY KEY,
            student_name TEXT,
            department_id INTEGER) """)

cur.execute("""
CREATE TABLE Departments (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT
)
""")
cur.executemany("insert into Students values (?,?,?)",
                [(1,"Sanjeev",22),(2,"Mohan",86),
                (3,"Rohan",87),(4,"Ram",None)])

cur.executemany("INSERT INTO Departments VALUES (?, ?)", [
    (22, "CSE"), (86, "ECE"), (88, "Mechanical")
])

queries = {
    "INNER JOIN": """
        SELECT s.student_id, s.student_name, d.department_name
        FROM Students s INNER JOIN Departments d
        ON s.department_id = d.department_id
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

