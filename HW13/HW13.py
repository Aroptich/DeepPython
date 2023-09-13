# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним классы исключения
# с выводом подробной информации. Поднимайте исключения внутри основного кода. Например, нельзя создавать прямоугольник
# со сторонами отрицательной длины.

# Задача с треугольником
from exeptions import *


class TriangleChecker:
    def __init__(self, a: int or float,  b: int or float, c: int or float) -> None:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
            raise TypeError('Аргументы должны быть или целыми или вещественными числами!')
        elif a > c + b or b > a + c or c > b + a:
            raise TriangleError("Невозможно построить треугольник по данным аргументам!")
        else:
            self.a = a
            self.b = b
            self.c = c
            print('Треугольник создан')

    def is_isosceles(self) -> str:
        """Проверка на равнобедренность"""
        if (self.a == self.b and self.b != self.c and self.a != self.c) or (
                self.c == self.b and self.b != self.a and self.c != self.a):
            return f'Треугольник равнобедренный!'
        else:
            return f'Треугольник неравнобедренный!'

    def is_fullside(self) -> str:
        """Проверка на равносторонность"""
        if self.a == self.b == self.c:
            return f'Треугольник равносторонний!'
        else:
            return f'Треугольник неравносторонний!'


# triangle = TriangleChecker(50, 2, 12)  # The triangle can't exist with such sides as: 50, 2, 12

# Напишите функцию для транспонирования матрицы



def transposing_matrix(array: list) -> list:
    """Функция принимает матрицу(вложенные списки) и возвращает транспонированную матрицу"""
    if all(isinstance(i, list) for i in array):
        return [list(line) for line in zip(*array)]
    else:
        raise MatrixError(f'Невозможно произвести транспонирование матрицы {array}!\n'
                          f'Матрица должна быть типа список в списке')


# matrix = [1, 2, 3]
# print(transposing_matrix(matrix))  # Input values must be list in list

# Например, нельзя создавать прямоугольник со сторонами отрицательной длины.



class Rectangle:

    def __init__(self, a: int or float, b: int or float) -> None:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError('Стороны должны быть целыми или вещественными числами!')
        if a <= 0 or b <= 0:
            raise RectangleError('Стророна прямоугольника должна быть больше нуля!')
        else:
            self.a = a
            self.b = b

    def __str__(self) -> str:
        return f'Class: {Rectangle.__name__}, first side={self.a}, second side={self.b}'


r1 = Rectangle('1', 2)  # ValueError: Стороны должны быть целыми или вещественными числами!
# r2 = Rectangle(-1488, 666)  # exeptions.RectangleError: Стророна прямоугольника должна быть больше нуля!
