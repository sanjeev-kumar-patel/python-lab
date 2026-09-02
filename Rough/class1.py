# Static Methods
class Student:
    @staticmethod
    def welcome():
        print("Welcome")
    

s = Student()
s.welcome()
Student.welcome()

# del s.welcome()
s.welcome()

