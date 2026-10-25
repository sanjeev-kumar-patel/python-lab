# Draw Labels, Grid, Subplot, Scatter, Bars, Pie charts using matplotlib

import matplotlib.pyplot as plt

students = ["Aman", "Riya", "Rahul", "Neha"]
marks = [85, 90, 78, 92]

hours = [1, 2, 3, 4, 5]
scores = [40, 50, 65, 75, 90]

subjects = ["Python", "Java", "C++", "DBMS"]
students_count = [30, 25, 20, 15]

fig, axes = plt.subplots(2, 2, figsize=(12, 9))

axes[0, 0].plot(students, marks, marker="o")
axes[0, 0].set_title("Student Marks")
axes[0, 0].set_xlabel("Students")
axes[0, 0].set_ylabel("Marks")
axes[0, 0].grid(True)

axes[0, 1].scatter(hours, scores)
axes[0, 1].set_title("Study Hours vs Scores")
axes[0, 1].set_xlabel("Study Hours")
axes[0, 1].set_ylabel("Scores")
axes[0, 1].grid(True)

axes[1, 0].bar(subjects, students_count)
axes[1, 0].set_title("Students per Subject")
axes[1, 0].set_xlabel("Subjects")
axes[1, 0].set_ylabel("Number of Students")
axes[1, 0].grid(axis="y")

axes[1, 1].pie(
    students_count,
    labels=subjects,
    autopct="%1.1f%%",
    startangle=90
)
axes[1, 1].set_title("Subject-wise Distribution")

plt.tight_layout()
plt.show()