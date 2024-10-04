# Программа-калькулятор для изучения возможностей Git
def sum(val1, val2):
    print("Сумма равна: ", a + b)
def razn(val1, val2):
    print("Разность равна: ", a - b)
def umn(val1, val2):
    print("Произведение равно: ", a * b)
def delen(val1, val2):
    print("Результат деления: ", a / b)
    #простой бесполезный комментарий
exit = False
while not exit:
    try:
        a = int(input ("Введите первое число: "))
        b = int(input ("Введите второе число: "))
        c = input("Введите знак действия ('+', '-', '/', '*'): ")
        exit_cucle = False
        if c == "*":
            umn(a,b)
            exit_cucle = True
        elif c=="+":
            sum(a,b)
            exit_cucle = True
        elif c=="-":
            razn(a,b)
            exit_cucle = True
        elif c=="/":
            delen(a,b)
            exit_cucle = True
        else:
            print("Ошибка: ввели неправильный знак действия!")
        if exit_cucle == True:
            d = input("Если хотите выйти, нажмите '1': ")
            if d == "1":
                exit = True
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")
    except ValueError:
        print("Ошибка: ввели символ!")