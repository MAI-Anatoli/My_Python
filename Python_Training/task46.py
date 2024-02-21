# Предложите пользователю ввести число. Продолжайте запрашивать число, пока введенное число не будет больше 5, после чего выведите сообщение «The last number you entered was a [число]» и остановите программу.

num = int(input("Enter a number: "))
while num <= 5:
  num = int(input("Enter a number: "))
  num = num + 1
print('The last number you entered was a', num)
