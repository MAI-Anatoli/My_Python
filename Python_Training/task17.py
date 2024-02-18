#Предложите пользователю 
#ввести его возраст. Если 
#введенное значение равно 
#18 и более, выведите сооб-
#щение «You can vote»; если 
#17 — сообщение «You can 
#learn to drive»; если 16 — 
#сообщение «You can buy a 
#lottery ticket». Если значение 
#меньше 16, выведите со-
#общение «You can go Trickor-Treating».

age = int(input('Cati ani ai?: '))
if age >= 18:
    print('You can vote')
elif age == 17:
    print(' You can learn to drive ')
elif age == 16:
    print('You can buy a lottery ticket»')
# elif age < 16:
else:
     print('You can go Trickor-Treating')
# else:
#     print('Nu ma intereseaza')            
        
        