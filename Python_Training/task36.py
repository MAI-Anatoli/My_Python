# Измените программу из упражнения 35 так, чтобы она предлагала
# пользователю ввести имя и число, а затем выводила имя заданное
# количество раз.

name = input('Enter a name: ')
num = int(input('Enter a number:'))
for _ in range(num):
  print(name)

##############################################

            # Решение с книги
            
name = input("Type in your name: ")
number = int(input("Enter a number: "))
for i in range(0, number):
    print(name)  