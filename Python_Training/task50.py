# Предложите пользователю ввести
# число от 10 до 20. Если введенное
# значение меньше 10, выведите
# сообщение «Too low» и
# предложите повторить попытку.
# Если введенное значение больше
# 20, выведите сообщение «Too
# high» и предложите повторить
# попытку. Повторяйте до тех пор,
# пока не будет введено значение из # диапазона от 10 до 20, после чего # выведите сообщение «Thank you».

user = int(input('Enter a number 10-20 : '))
while user < 10:
  print('Too low')
  user = int(input('Enter a number 10-20 : '))

while user > 20:
  print('Too high')
  user = int(input('Enter a number 10-20 : '))

if user >= 10 and user <= 20:
  print('Thank you')
