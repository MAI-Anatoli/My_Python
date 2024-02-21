num = 10
while num > 0:
  print(f'There are {num} green bottles hanging on the wall, {num} green bottles hanging on the wall, and if 1 green bottle should accidentally fall')
  num -= 1
  user = int(input('How many green bottles will be hanging on the wall? '))
  while user != num:
    print('No, try again')
    user = int(input('How many green bottles will be hanging on the wall? '))
print('There are no more green bottles hanging on the wall')
