# Создайте переменную с именем comp_num и присвойте ей
# значение 50. Предложите пользователю ввести число. 
# Пока предположение не совпадает
# со значением comp_num, сообщите, больше оно или меньше
# comp_num, и предложите ввести
# другое число. Если введенное
# значение совпадет с comp_num,
# выведите сообщение «Well done,
# you took [попытки] attempts».


comp_num = 50
user_num = int(input('Enter a num: '))
count = 1

while user_num < comp_num:
   print('Try entering a higher number =>')       
   user_num = int(input('Enter a num =>: ')) 
   count += 1

if user_num > comp_num:
      print('Try entering a lower number <=')
      user_num = int(input('Enter a num <=: '))
      count += 1

if user_num == comp_num:
  print(f'Well done, you took, {count} attempts') 

##########################################################

                  # Решение с книги
                  
comp_num = 50
guess = int(input("Can you guess the number I am thinking of? "))
count = 1
while guess != comp_num:
      if guess < comp_num:
            print("Too low")
else:
    print("Too high")
    count = count + 1
    guess = int(input("Have another guess: "))
    print("Well done, you took ", count, " attempts")