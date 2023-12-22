import math 

def square(side):
  square_area = side * side 
  return math.ceil(square_area) 

side = 5.5
result = square(side)

print('Площадь квадрата:', result)