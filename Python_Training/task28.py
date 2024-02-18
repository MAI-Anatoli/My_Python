#Измените программу из задачи 027 так, чтобы она 
#выводила результат с точностью до двух знаков 
#в дробной части.

# import math

# num = float(input('Number float: '))
# result = num * 2
# rezultat = math.sqrt(result)
# print(rezultat)

########################################################

                    # Решения из книги

num = float(input("Enter a number with lots of decimal places: "))
answer = num*2
print(answer)
print (round(answer, 2))
