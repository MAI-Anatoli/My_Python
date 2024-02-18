#Предложите пользователю 
#ввести два числа. Если первое 
#число больше второго, сна-
#чала выведите второе число, 
#а потом первое. В противном 
#случае выведите сначала пер-
#вое число, а потом второе.

number1 = int(input('Number 1: '))
number2 = int(input('Number 2: '))
if number1 > number2:
    print(number2, number1)
else:
        print(number1, number2)