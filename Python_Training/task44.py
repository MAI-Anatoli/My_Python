# Спросите у пользователя, скольких людей он хочет пригласить на вечеринку. Если будет введено
# число меньше 10, запросите имена и после каждого имени выведите строку «[имя] has been invited».
# Если введенное число больше или равно 10, выведите сообщение «Too many people».

people_to_the_party = int(
    input('Сколько людей хотите пригласить на вечерин: '))
if people_to_the_party < 10:
  for i in range(people_to_the_party):
    name = input('Введите имя: ')
    print(f'{name} has been invited')
else:
  print('Too many people')
