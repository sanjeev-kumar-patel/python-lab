# P1: Demonstrate operator overloading by adding
# two points p1(x1,y1) + p2(x2,y2)
class Point:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    def __add__(self, nextPoint):
        return Point(self.x + nextPoint.x, self.y + nextPoint.y)
    def display(self):
        print("Point: ", f"({self.x}, {self.y})")
p1 = Point(2,5)
p2 = Point(3,6)
p3 = p1 + p2
p3 = p1 + p2
print("First Point:")
p1.display()
print("Second Point:")
p2.display()
print("After Addition:")
p3.display()