# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.
import string


def hex_number(number: int) -> str:
    """Функция получает целое число.
    Возвращает целое число в шестнадцатиричном представлении
    """
    CONST_HEX = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')
    PREFIX = '0x'
    DIVIDER = 16
    HEX_NUMBER = ''
    try:
        if not isinstance(number, int):
            raise TypeError('Вводимый аргумент должен быть целым числом ')
        if number < 0:
            PREFIX = '-' + PREFIX
        while abs(number) >= 1:
            HEX_NUMBER += CONST_HEX[abs(number) % DIVIDER]
            number = abs(number) // DIVIDER
        return f'{PREFIX}{HEX_NUMBER[::-1]}'
    except Exception as err:
        print(err)
        return -1


# print(hex_number('-500'))

# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

def main(value1: str, value2: str) -> str:
    return f'{sum(value1, value2)}, {multy(value1, value2)}'

def is_valid(value: str) -> bool:
    """Функция проверят является ли значение строкой вида 'a/b'.
    Возвращает True или False"""
    if not isinstance(value, str):
        raise TypeError('Аргумент должен быть строкой')

    return bool(value.count('/'))


def sum(value1: str, value2: str) -> str:
    """Функция принимает 2 аргумента типа 'a/b'.
        Возвращает сумму 2-х аргоментов"""
    if is_valid(value1) and is_valid(value2):
        sum_values = [arr1+arr2 for arr1,arr2 in zip(list(map(int,value1.split('/'))),
                                                     list(map(int,value2.split('/'))))]
        return '/'.join(list(map(str, sum_values)))


def multy(value1: str, value2: str) -> str:
    """Функция принимает 2 аргумента типа 'a/b'.
    Возвращает произведение 2-х аргоментов"""
    if is_valid(value1) and is_valid(value2):
        multy_values = [arr1*arr2 for arr1,arr2 in zip(list(map(int,value1.split('/'))),
                                                     list(map(int,value2.split('/'))))]
        return '/'.join(list(map(str, multy_values)))



if __name__ == '__main__':
    print(main('3/4', '5/7'))
    print(hex_number(-500))

