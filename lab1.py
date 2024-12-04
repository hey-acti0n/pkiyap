import math

def solve_biquadratic(a, b, c):
    
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        return "Нет действительных решений"
    
    y1 = (-b + math.sqrt(discriminant)) / (2*a)
    y2 = (-b - math.sqrt(discriminant)) / (2*a)
    
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


a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

result = solve_biquadratic(a, b, c)
print("Решения:", result)
