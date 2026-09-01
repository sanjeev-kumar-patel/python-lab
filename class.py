# marks = input("enter marks : ")
# try: 
#     if marks < 0 or marks > 100:
#         raise Exception("Enter marks in range: ")
# except Exception:
#     print(Exception) 
# else:
#     print(marks)
    
# class InvalidMarks(Exception):
#     pass
# marks = 200
# try:
#     if marks<0 or marks>100:
#         raise InvalidMarks
# except InvalidMarks:
#     print("marks are not in range")

class Student:
    college = "NIT Srinagar" #cless attribute
    def __init__(self,name,rno, marks):
        self.name = name   #instance attribute
        self.rno = rno
        self.marks = marks
        self.college = "Abc"
    def welcome(self):
        
        print("Welcome",self.name)
    def getMarks(self):
        print("Hello",self.name, "your marks are",self.marks)
s1 = Student("Sanjeev",22,34)
print(s1.welcome())
print(s1.name)
print(s1.rno)
s1.getMarks()



# create objects of 5 students and enter the marks of 5 subjetcs. 
# define the methods for average marks.

class Student:
    def __init__(self,name):
        self.name = name
        self.marks = []
    def enterMarks(self):
        for i in range(0,5):
            mark = int(input(f"Enter marks {i+1} : "))
            self.marks.append(mark)
    def averageMarks(self):
        return sum(self.marks)/5

students = []
for i in range(0,5):
    name = input("Enter Student Name {i+1} ")
    student = Student(name)
    student.enter_marks()
    students.append(student)
for student in students:
    print(student)
    
    















class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def enter_marks(self):
        for i in range(5):
            mark = float(input(f"Enter marks of subject {i + 1}: "))
            self.marks.append(mark)

    def average(self):
        return sum(self.marks) / 5


students = []

for i in range(5):
    print(f"\nEnter details of Student {i + 1}")
    name = input("Enter name: ")

    student = Student(name)
    student.enter_marks()

    students.append(student)


print("\nStudent Average Marks")

for student in students:
    print(f"{student.name}: {student.average():.2f}")
    