
import math
from math import pi

class biquadratic:
    def __init__(self, a=0,b=0,c=0):
        print("Введите коэфициент A")
        self.a=float(input())
        print("Введите коэфициент B")
        self.b=float(input())
        print("Введите коэфициент C")
        self.c=float(input())

    def solve(self):
        discriminant = self.b**2 - 4*self.a*self.c
        if discriminant < 0:
            return "Нет действительных решений" 
        y1 = (-self.b + math.sqrt(discriminant)) / (2*self.a)
        y2 = (-self.b - math.sqrt(discriminant)) / (2*self.a)      
        solutions = []       
        if y1 >= 0:
            solutions.append(math.sqrt(y1))
            solutions.append(-math.sqrt(y1))       
        if y2 >= 0:
            solutions.append(math.sqrt(y2))
            solutions.append(-math.sqrt(y2))       
        if not solutions:
            return "Нет действительных решений"
        
        return solutions




equation=biquadratic()
print(equation.solve())



