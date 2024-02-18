#Предложите пользователю ввести радиус круга (рас-
#стояние от центра до внешней границы.) Вычислите 
#площадь круга (π * радиус2).

# import math 

# math_1 = math.pi * 2
# print(math_1)

###################################

                # Решения из книги

import math
radius = int(input("Enter the radius of the circle: "))
area = math.pi * (radius**2)
print(area)
