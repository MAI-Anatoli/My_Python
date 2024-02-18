# Предложите пользователю ввести имя и фамилию в нижнем
# регистре. Преобразуйте строки к титульному регистру и со-
# едините их. Выведите полученный результат.

name = input('Enter a name: ')
surname = input('Enter a surname: ')
name1 = str.title(name)
surname1 = str.title(surname)
result = name1+surname1
print(result)



# Решения с книги

firstname = input("Enter your first name in lowercase: ")
surname = input("Enter your surname in lowercase: ")
firstname = firstname.title()
surname = surname.title()
name = firstname + " " + surname
print(name)