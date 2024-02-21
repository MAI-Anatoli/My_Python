#Предложите пользователю ввести сначала одно число, а затем другое. Сложите два числа и спросите, хочет ли он прибавить еще одно. Если он введет «y», предложите ввести еще одно число; это продолжается до тех пор, пока пользователь не введет ответ «y». После того как цикл остановится, выведите сумму.
# Consider this snippet from ./task47.py

num = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
sum = num + num2
result = input("Do you want to add another number? (y/n): ")
while result == "y":
  num3 = int(input("Enter a number: "))
  sum = sum + num3
  result = input("Do you want to add another number? (y/n): ")
  if result == "n":
    print(sum)
