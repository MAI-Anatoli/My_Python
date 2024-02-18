# Предложите пользователю ввести сначала имя,
# а затем фамилию. Соедините их, разделив про-
# белом, после чего выведите полное имя и его
# длину.


# мое решение
name = input('Enter a name: ')
surname = input('Enter a surname: ')
result = name+' '+surname               
print(name, surname, '\n',len(result))  


# решения с книги

# firstname = input("Enter your first name: ")
# surname = input("Enter your surname: ")
# name = firstname + " " + surname
# length = len(name)
# print(name)
# print(length)