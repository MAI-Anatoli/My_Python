# Выведите строки «There are [счетчик] green bottles hanging on the wall, [счетчик] green bottles 
# hanging on the wall, and if 1 green bottle should accidentally fall». Затем выведите вопрос: «how many 
# green bottles will be hanging on the wall?». Если пользователь ответит правильно, выведите сообщение 
# «There will be [счетчик] green bottles hanging on the wall». Если пользователь ответит неправильно, 
# выведите сообщение «No, try again», пока не будет дан правильный ответ. Когда счетчик уменьшится до 0, 
# выведите сообщение «There are no more green bottles hanging on the wall».


num = 15
while num > 0:
    print(f'На стене стоят', num, 'зеленые бутылки', num,
      ' зеленые бутылки на стене стоят, если 1 нечайно бутылка упадет')
num -= 1
question = int(input('\nСколько зеленые бутылки будут стоять на стене? : '))
print('На стене будут стоять', {num},' зеленые бутылки.')
while question != num:
       print('Нет, попробуй еще раз')
question = int(input('\nСколько зеленые бутылки будут стоять на стене? : '))

print('На стене больше нет зеленые бутылки.')