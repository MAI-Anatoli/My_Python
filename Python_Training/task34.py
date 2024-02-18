# Выведите следующее сообщение:
# 1) Square
# 2) Triangle
# Enter a number:
# Если пользователь вводит 1, программа запрашивает 
# длину стороны квадрата и выводит его площадь. Если 
# пользователь вводит 2, программа запрашивает длину 
# стороны и высоту треугольника, проведенную к этой 
# стороне, после чего выводит его площадь. 
# Если пользователь вводит что-то другое, программа должна
# выдать подходящее сообщение об ошибке.

# num = float(input('Enter numbers: '))
# if num == 1:
#     square = float(input('Enter a number square: '))
#     result = square * 4
# elif num == 2:
#     triangle = float(input('Enter triangle length: '))
#     triangle1 = float(input('Enter triangle height: '))
#     result = triangle * triangle1
# else:
#     result = 'Try again'
    
# print(result)
    
#######################################################################
                
                # Решения из книги
                
print("1) Square")
print("2) Triangle")
print()
menuselection = int(input("Enter a number: "))
if menuselection == 1:
    side = int(input("Enter the length of one side: "))
    area = side * side
    print("The area of your chosen shape is ", area)
elif menuselection == 2:
    base = int(input("Enter the length of the base: "))
    height = int(input("Enter the height of the triangle: "))
    area = (base * height) / 2
    print("The area of your chosen shape is ", area)
else:
    print("Incorrect option selected")    
    
    
    
    

