# Программа-калькулятор для изучения возможностей Git
def sum(val1, val2):
    print("Сумма равна: ", a + b)
def razn(val1, val2):
    print("Разность равна: ", a - b)
def umn(val1, val2):
    print("Произведение равно: ", a * b)
def delen(val1, val2):
    print("Результат деления: ", a / b)
exit = False
while True:
    try:
        a = int(input ("Введите первое число: "))
        b = int(input ("Введите второе число: "))
        c = input("Введите знак действия ('+', '-', '/', '*'): ")
        if c == "*":
            umn(a,b)
            break
        elif c=="+":
            sum(a,b)
            break
        elif c=="-":
            razn(a,b)
            break
        elif c=="/":
            delen(a,b)
            break
        else:
            print("Ошибка: ввели неправильный знак действия!")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")
    except ValueError:
        print("Ошибка: ввели символ!")