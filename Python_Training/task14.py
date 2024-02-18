#Предложите пользователю 
#ввести число от 10 до 20 (вклю-
#чительно). Если будет введено 
#число из этого диапазона, вы-
#ведите сообщение «Thank you»; 
#в противном случае выведите 
#сообщение «Incorrect answer».

number = int(input('Number 10 - 20: '))
if number in range(10, 20):
    print('Thank you')
else:
    print('Incorrect answer')