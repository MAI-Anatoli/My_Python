# Предложите пользователю 
# ввести имя и число.
# Если число меньше 10,
# программа должна вывести имя 
# заданное количество раз; 
# в противном случае она выводит
# сообщение «Too high»
# три раза.

name = input("Введите имя: ")
num = int(input("Введите число: "))
for i in range(num):
  if num < 10:
    print(name)
for i in range(3):
  print("Too high")


################################################

                # Решение с книги
                
name = input("Enter your name: ")
num = int(input("Enter a number: "))
if num < 10:
  for i in range(0, num):
    print(name)
else:
  for i in range(0, 3):
    print("Too high")