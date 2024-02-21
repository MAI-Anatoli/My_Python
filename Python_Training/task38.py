# Измените программу
# из упражнения 37 так,
# чтобы она также запрашивала число. 
# Выведите имя (по одной букве
# в каждой строке) и по-
# вторите вывод равное
# введенному числу количество раз.

name = input('Enter name: ')
mum = int(input('Enter number: '))
for i in name:
  for _ in range(mum):
    print(i)

###########################################

            # Решение с книги
            
num = int(input("Enter a number: "))
name = input("Enter your name: ")
for x in range(0, num):
  for i in name:
    print(i)