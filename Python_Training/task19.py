#Предложите пользователю ввести значение 1, 2 или 3. Если вве-
#дено значение 1, выведите сообщение «Thank you»; если 2 — со-
#общение «Well done»; если 3 — сообщение «Correct». Если введено 
#любое другое значение, выведите сообщение «Error message».

number = int(input('Numar de la 1 Pana la 3: '))
if number == 1:
    print('Thank you')
elif number == 2:
    print('Well done')
elif number == 3:
    print('Correct')
else:
    print('Error message')