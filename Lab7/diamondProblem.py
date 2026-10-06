class Person:
    def show(self):
        print("Class Person")
class Mother(Person):
    def show(self):
        print("Class Mother")
class Father(Person):
    def show(self):
        print("Class Father")
class Child(Mother, Father):
    pass
obj = Child()
obj.show()