# Task 1
# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c — стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
# с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним,равнобедренным или равносторонним


def existence_triangle(a: int | float, b: int | float, c: int | float):
    """функция принимает на вход 3 аргумента и выполняет проверку
    по их значениям  на существование треугольгика """
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
            raise Exception('Аргументы должны быть целыми или вещественными числами')
        if a > b + c or b > a + c or c > a + b:
            raise Exception('Такого треугольника не существует')
        else:
            print('Треугольник существует')
    except Exception as error:
        print(error)


# existence_triangle(1,2,3)
# Task 2
# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
#
def prime_or_composite_number():
    '''Функция проверяет  натуральное положительное число
     является ли оно простое или составное'''
    try:
        number = int(input('Введите число: '))
        if number < 2 or number > 100_000:
            raise Exception(f"Число {number} не входит в диапазон от 2 до 100 000")
        i = 2
        count = 0
        while i ** i < number:
            if number % i == 0:
                count += 1
            i+=1
        if count == 0:
            print(f'Число {number} простое!')
        else:
            print(f'Число {number} составное!')
    except Exception:
        print('Число должно быть целым!')

