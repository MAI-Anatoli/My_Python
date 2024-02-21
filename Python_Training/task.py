comp_num = 50
user_num = int(input('Enter a num: '))
count = 1

while user_num < comp_num:
   print('Try entering a higher number =>')       
   user_num = int(input('Enter a num =>: ')) 
   count += 1

if user_num > comp_num:
      print('Try entering a lower number <=')
      user_num = int(input('Enter a num <=: '))
      count += 1
  
if user_num == comp_num:
  print(f'Well done, you took, {count} attempts') 

