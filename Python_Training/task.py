num = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
sum = num + num2
result = input("Do you want to add another number? (y/n): ")
while result == "y":
  num3 = int(input("Enter a number: "))
  sum = sum + num3
  result = input("Do you want to add another number? (y/n): ")
  if result == "n":
    print('Sum: ',sum)
