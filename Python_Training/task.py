
user = int(input('Enter a number 10-20 : '))
while user < 10:
    print('Too low')
    user = int(input('Enter a number 10-20 : '))
    
while user > 20:
    print('Too high')
    user = int(input('Enter a number 10-20 : ')) 
    
if user >= 10 and user <= 20:
    print('Thank you')