import colorama # на это не сомтри пока 

# так блэть самое просто что нужно знать о функциях это то что 
# функция это многократно используенмый блок кода 


# так первое что нужно запомнить функция сначало определяеться а потом вызываеться
# да блэт я капитан очивидность 

def age_a(): # определение функции
   # это самая простая функция
    print("hi world")              # набор инструкций данной функции
    print("ты создал MAGNUM OPUS") # проще говоря это тело 

def black(x): # ну тут уже понятно что я сделал?
    # если ты попытаешся запихнуть в эту функцию два аргумента то питухон разгруит тебе товарняк в лицо 
    print ("квадрат числа ",x,"=",x**2)

def danilpedro(x, y): # ладно это всё весело и не сложно 
    print(x * y)

def pedro(a): # и да это опять функция но с условными операторами 
    if a %2==0:
        print( a + "чило чётное") # да ладно )
    else: 
        print("я расскажу тебе сказку про паровозик котрый смог")
def num(b):
    pr=1
    for i in range (2,b+1): # это цикл но пока ещё рано это будет следуещим 
        pr=pr*i
    print(pr)

# так это были не сложные вареанты создания функций 
    # хотя о кокой сложности я говарю это ж петухон 
# создам условный оператор 
if 999>8:  # так это условный оператор и если значение верное то выполница первый вариант функции 
    def danil():
        print("Чел рости большой")

else:
        def danil(): # ну а если значение не верное то выполницы другой вариант фукции
        print("Чел рости очень  большой")




# что-бы не теряться ниже оосновной код там и вызываешь функции 
    # я опять капитан очевиднось 
black(15) # тут ты присврил значение 
danilpedro(13, 14) 
pedro(99)
num(9)
danil() # почему тут пусто да потому что данная функция не принемает значения 
