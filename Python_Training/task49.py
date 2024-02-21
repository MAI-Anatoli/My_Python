# Создайте переменную с име-
# нем compnum и присвойте ей
# значение 50. Предложите поль-
# зователю ввести число. Пока
# предположение не совпадает
# со значением compnum, сооб-
# щите, больше оно или меньше
# compnum, и предложите ввести
# другое число. Если введенное
# значение совпадет с compnum,
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

