# Предложите пользователю ввести имя человека, которого
# пользователь хочет пригласить на вечеринку. После этого вы-
# ведите сообщение «[имя] has been invited» и увеличьте счет-
# чик на 1. Спросите, хочет ли пользователь пригласить кого-то
# еще. Продолжайте запрашивать имена, пока пользователь не
# ответит отрицательно, и выведите количество приглашенных.

guest_name = input('Enter guest name: ')
count = 1
print(guest_name,'has been invited')
guests = input('would you like to invite someone else? y/n: ')
while guests == 'y':
    guest_name = input('Enter guest name: ')
    print(guest_name,'has been invited' )
    guests = input('would you like to invite someone else? y/n: ')
    count += 1
if guests == 'n':
        print(count)

##########################################################################

                # Решение с книги
                
again = "y"
count = 0
while again == "y":
    name = input("Enter a name of somebody you want to invite to the party: ")
print(name, " has been invited")
count = count + 1
again = input("Do you want to invite somebody else? (y/n) ")
print("You have ", count, " people coming to your party")