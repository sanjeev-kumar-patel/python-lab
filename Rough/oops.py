# Inheritance
class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        
    def printname(self):
        print(self.fname,self.lname)
    def welcome(self):
        print("welcome to the portal")

class Student(Person):
    def __init__(self,fname,lname,rno):
        # Person.__init__(self,fname,lname)
        super().__init__(fname,lname) 
        self.rno = rno
    def printname(self):
        # Person.__init__(self,fname,lname)
        super().printname()
        print(self.rno)

s = Student("Sanjeev","Patel",123)
s.printname()


# multilevel Inheritance
class GrandParent:
    def gparent(self):
        print("I am Gparent")
class Parent(GrandParent):
    def Parent(self):
        print("I am Parent")
class Child(Parent):
    def child(self):
        print("I am the child")
        
c = Child()
c.child()
c.Parent()
c.gparent()

# Multiple Inheritance

class A:
    def method(self):
        print("I'm in class A")
class B:
    def method(self):
        print("I'm in class B")
class C(A,B):
    pass
    def method(self):
        print("I'm in class C")

c = C()
c.method()