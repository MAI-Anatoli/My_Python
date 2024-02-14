# Предложите пользователю ввести число больше 100, а затем число меньше 10. Со-
# общите, сколько раз меньшее число помещается в большем, в удобном формате


numbers_1 = int(input('Numbers => 100: '))
numbers_2 = int(input('Numbers <= 10: '))
result = numbers_1 // numbers_2
print(result)
