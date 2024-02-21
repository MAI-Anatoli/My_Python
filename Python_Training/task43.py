# Спросите у пользователя, в каком направлении он хочет вести отсчет 
# (в прямом или обратном)
# Если выбран прямой отсчет, запросите число и проведите отсчет от 1 
# до введенного числа.
# Если выбран обратный отсчет, запросите число меньше 20, 
# а затем проведите обратный отсчет от 20 до заданного числа.
# Если введено что-то другое, выведите сообщение «I don’t understand»

direction = input('В каком направлении вы хотите вести отсчет?: ')
if direction == 'прямой ':
  number = int(input('Введите число: '))
  for i in range(1, number + 1):
    print(i)

elif direction == 'обратный':
  number = int(input('Введите число меньше 20: '))
  for i in range(20, number - 1, -1):
    print(i)

else:
  print('I don\'t understand')

#######################################################################

		# Решение с книги
  
direction = input("Do you want to count up and down? (u/d) ")
if direction == "u":
  num = int(input("What is the top number? "))
for i in range(1, num + 1):
      print(i)
      
      
      
elif direction == "d":
num = int(input("Enter a number below 20: "))
for i in range(20, num + 1, -1):
      print(i)
else:
    print("I don t understand")