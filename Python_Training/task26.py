# В шифре «поросячья латынь» начальная согласная
# буква слова перемещается в конец слова, и к ней до-
# бавляется суффикс «ay». Если слово начинается с глас-
# ной, к нему просто добавляется суффикс «way». Напри-
# мер, pig превращается в igpay, banana — в ananabay,
# а aardvark — в aardvarkway. Напишите программу,
# которая предлагает пользователю ввести слово и пре-
# образует его в «поросячью латынь». Проследите за тем,
# чтобы новое слово выводилось в нижнем регистре

#  гласные   = «A», «E», «I», «O», «U», «Y»
#  согласные = «B», «C», «D», «F», «G», «H», «J», «K», «L», «M», «N», 
# «P», «Q», «R», «S», «T», «V», «W», «X», «Y», «Z».

# word = input('Enter a word: ')
# vowels = 'aeiouAEIOU'
# if word[0] in vowels:
#     print(str.lower(word + 'way'))
# else:
#     print(str.lower(word[1:] + word[0] + 'ay'))
    
    
    
    
word = input("Please enter a word: ")
first = word[0]
length = len(word)
rest = word[1:length]
if first != "a" and first != "e" and first != "i" and first != "o" and first != "u":
    new_word = rest + first + "ay"
else:
    new_word = word + "way"
print(new_word.lower())

