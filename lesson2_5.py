'''
https://drive.google.com/file/d/15Xt2S6YHrGTG3cB_mzBjEa676TkBC4-i/view?usp=sharing

Вывести на экран коды и символы таблицы ASCII,
начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.


'''

q = 0
for i in range(32, 128):
    print(f'{i} - {chr(i)}, ', end='')
    q += 1
    if q == 10:
        print('\n')
        q = 0
