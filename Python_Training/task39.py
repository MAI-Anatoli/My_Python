# Предложите пользователю ввести число от 1
# до 12. Выведите таблицу умножения для этого
# числа.

num = int(input('Enter a number: '))
for i in range(1, 12):
  print(f'{num} * {i} = {num * i}')
