# Предложите пользователю ввести
# число от 10 до 20. Если введенное
# значение меньше 10, выведите
# сообщение «Too low» и
# предложите повторить попытку.
# Если введенное значение больше
# 20, выведите сообщение «Too
# high» и предложите повторить
# попытку. Повторяйте до тех пор,
# пока не будет введено значение из 
# диапазона от 10 до 20, после чего 
# выведите сообщение «Thank you».

user = int(input('Enter a number 10-20 : '))
while user < 10:
  print('Too low')
  user = int(input('Enter a number 10-20 : '))

while user > 20:
  print('Too high')
  user = int(input('Enter a number 10-20 : '))

if user >= 10 and user <= 20:
  print('Thank you')

#########################################################

                # Решение с книги
                
num = int(input("Enter a number between 10 and 20: "))
while num < 10 or num > 20:
  if num < 10:
    print("Too low")
else:
  print("Too high")
num = int(input("Try again: "))
print("Thank you")