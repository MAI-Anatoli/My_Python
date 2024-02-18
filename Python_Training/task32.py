#Предложите пользователю ввести радиус 
#и высоту цилиндра. Вычислите его объем 
#(площадь круга * высота) и выведите его 
#с точностью до трех знаков.

# radius = float(input('Enter radius:'))
# cylinder_height = float(input('Enter height: '))
# result = radius * cylinder_height
# print(result)

##########################################################

                        # Решения с книги

import math
radius = int(input("Enter the radius of the circle: "))
depth = int(input("Enter depth: "))
area = math.pi * (radius**2)
volume = area * depth
print(round(volume,3))

