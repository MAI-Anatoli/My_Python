# Присвойте переменной с именем total значение 0. Предложите
# пользователю ввести пять чисел, и после каждого ввода спрашивайте, 
# хочет ли он включить это число в суммирование. Если ответ будет
# положительным, прибавьте введенное число к total. Если же ответ
# будет отрицательным, число к total не прибавляется. После ввода
# всех пяти чисел выведите значение total.

total = 0
for i in range(5):
  num = int(input("Enter a number: "))
  answer = input("Do you want to include this number? ")
  if answer == "yes":
    total += num
print(total)

####################################################################

                # Решение с книги
                
total = 0
for i in range(0, 5):
  num = int(input("Enter a number: "))
ans = input("Do you want this number included? (y/n) ")
if ans == "y":
  total = total + num
print(total)