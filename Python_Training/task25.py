# Предложите пользователю ввести имя. Если длина имени
# меньше 5 символов, предложите ввести фамилию, соедините
# их (без пробела) и выведите полное имя в верхнем регистре.
# Если длина имени составляет 5 и более символов, выведите
# имя в нижнем регистре.

name = input('Enter a name: ')
num = len(name)
if num < 5:
  surname = input('Enter a surname: ')
  res = name+surname
  result = str.upper(res)
elif num >= 5:
    result = str.lower(name)
    
print(result)
