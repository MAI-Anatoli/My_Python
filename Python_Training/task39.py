# Предложите пользователю ввести число от 1
# до 12. Выведите таблицу умножения для этого
# числа.

num = int(input('Enter a number: '))
for i in range(1, 12 +1):
  print(f'{num} * {i} = {num * i}')


###########################################

        # Решение с книги
        
num = int(input("Enter a number between 1 and 12: "))
for i in range(1, 13):
  answer = i * num
print(i, "x", num, "=", answer)     