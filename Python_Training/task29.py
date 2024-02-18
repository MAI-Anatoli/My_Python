#Предложите пользователю ввести целое число боль-
#ше 500. Вычислите квадратный корень из этого числа 
#и выведите его с точностью до двух знаков в дробной 
#части.

# import math 
# num = int(input('Enter number min 500: '))
# result = math.sqrt(num)
# print(result)

######################################################

                # Решения из книги

import math
num = int(input("Enter a number over 500: "))
answer = math.sqrt(num)
print(round(answer, 2))

