#Спросите пользователя, идет ли дождь. Преобразуйте его ответ к нижнему реги-
#стру. Если пользователь ответит «yes», спросите, ветрено ли на улице. Если поль-
#зователь ответит «yes» и на второй вопрос, выведите сообщение «It is too windy 
#for an umbrella»; в противном случае выведите сообщение «Take an umbrella». 
#Если же пользователь не дал положительного ответа на первый вопрос, выведи-
#те сообщение «Enjoy your day».

weather = input('Ploua afara? yes or no: ')
weather = str.lower(weather)
if weather == 'yes':
        wyrt = input('Bate vântul? yes or no: ')
        wyrt = str.lower(wyrt)
        if wyrt == 'yes':
            print('umbrella')
        else: 
            print('Take an umbrella') 
else:
           print('Enjoy your day  ')
    