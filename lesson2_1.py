'''
https://drive.google.com/file/d/15Xt2S6YHrGTG3cB_mzBjEa676TkBC4-i/view?usp=sharing

Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе
символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
программа должна сообщать об ошибке и снова запрашивать знак операции.
Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.
'''


print('Введите два числа и знак операции над ними')
while True:
    a = int(input('Введите число 1: '))
    b = int(input('Введите число 2: '))
    c = input('Введите знак операции: ')
    if c == '0':
        print('Досвидания')
        break
    if b == 0:
        if c == '*' or c == '+' or c == '-':
            print(f'{0.0}')
            continue
        print('На ноль делить нельзя')
        continue
    if c != '*' and c != '/' and c != '+' and c != '-':
        print('Вы ввели не верный знак операции. Попробуйте еще')
    if c == '*':
        print(f'{a * b}')
    if c == '/':
        print(f'{a / b}')
    if c == '+':
        print(f'{a + b}')
    if c == '-':
        print(f'{a - b}')
