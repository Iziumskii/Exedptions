def addition(data):
    print(int(data[1]) + int(data[2]))


def subtraction(data):
    print(int(data[1]) - int(data[2]))


def multiplication(data):
    print(int(data[1]) * int(data[2]))


def division(data):
    print(int(data[1]) / int(data[2]))


def operation_definition(data):
    if data[0] == '+':
        addition(data)
    elif data[0] == '-':
        subtraction(data)
    elif data[0] == '*':
        multiplication(data)
    elif data[0] == '/':
        division(data)


command = input('Введите данные: ')

assert command[0] in ('+', '-', '*', '/'), "Вы ввели неверные данные"
assert (len(command) == 3), "Вы ввели невернное кол-во символов"

try:
    operation_definition(command)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
# except IndexError as e:
#    print(e)
