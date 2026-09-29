# P2: Add two fractions f1 = (x1/y1), f2 = (x2/y2)

from math import gcd
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def __add__(self, other):
        num = (self.numerator * other.denominator) + \
              (other.numerator * self.denominator)
        den = self.denominator * other.denominator
        g = gcd(num, den)
        return Fraction(num // g, den // g)
    def display(self):
        print(self.numerator, "/", self.denominator)

f1 = Fraction(1, 2)
f2 = Fraction(1, 3)

f3 = f1 + f2

print("First Fraction:")
f1.display()

print("Second Fraction:")
f2.display()

print("Addition:")
f3.display()