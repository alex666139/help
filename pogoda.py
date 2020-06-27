# импорт бибиотек 
from pyowm import OWM
import colorama 

# токен для модуля pyOWM
owm = OWM("03afb3cf29c26cfcc3b9a347b709d308")
# определение функций 

def calc(): # функция калькулятора 
    calc_what = input("что делаем + - * / ") # запрос пользевателю
    a = input("первое число ")
    b = input("второе число ")
    # условный оператор 
    if calc_what == "+":    # сложение 
        c = (int(a)) + (int(b))
        print("ответ" + c)

    elif calc_what == "-":  # вычитание 
        c = (int(a)) - (int(b))
        print("ответ" + c)
    
    elif calc_what == "*":  # умножение 
        c = (int(a)) * (int(b))
        print("ответ" + c)
    
    elif calc_what == "/":  # деление 
        c = (int(a)) / (int(b))
        print("ответ" + c)

    else:                   # ошибка 
        print("ошибка 404")
    return
    
def pogoda(): # функция которая покажет рогода 
    sity = input("укажите ваш город ")
    observation = owm.weather_at_place( sity ) # запрос на поиск города
    w = observation.get_weather()
    print("В городе" + sity + "сейчас" + w)
    return

# основной код 
waht = input("погода калькулятор ")
# условный оператор 
if waht == "калькулятор":
    calc() # вызов функции
elif waht == "погода":
    pogoda() # вызов функции
else:
    print('что то пошло не так')
    

    



