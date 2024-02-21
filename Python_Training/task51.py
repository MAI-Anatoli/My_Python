# Выведите строки «There are [счетчик] green bottles hanging on the wall, [счетчик] green bottles 
# hanging on the wall, and if 1 green bottle should accidentally fall». Затем выведите вопрос: «how many 
# green bottles will be hanging on the wall?». Если пользователь ответит правильно, выведите сообщение 
# «There will be [счетчик] green bottles hanging on the wall». Если пользователь ответит неправильно, 
# выведите сообщение «No, try again», пока не будет дан правильный ответ. Когда счетчик уменьшится до 0, 
# выведите сообщение «There are no more green bottles hanging on the wall».


num = 15
print(f'\nНа стене стоят', num, 'зеленые бутылки', num,
      'зеленые бутылки на стене стоят, если 1 нечайно бутылка упадет')
question = int(input('\nСколько зеленые бутылки будут стоять на стене?: '))
while question != num:
      num -= 1
      print('На стене будут стоять', {num},' зеленые бутылки.')
      while question > num or question < num:
            print('\nНет, попробуй еще раз')
            question = int(input('\nСколько зеленые бутылки будут стоять на стене? : '))
      if num == 0:
            print('На стене больше нет зеленые бутылки.')
      
###################################################################################################

                  # Решение с книги
                  
          
num = 10
while num > 0:
      print("There are ", num, " green bottles hanging on the wall.")
      print( num, " green bottles hanging on the wall.")
      print("And if 1 green bottle should accidentally fall,")
      num = num - 1
      answer = int(input("How many green bottles will be hanging on the wall? "))
      if answer == num:
            print("There will be ", num, " green bottles hanging on the wall.")
      else:
            while answer != num:
                  answer = int(input("No, try again: "))
print("There are no more green bottles hanging on the wall.")
