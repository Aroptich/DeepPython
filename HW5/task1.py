#Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
#Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
import os.path
def split_path(path: str) -> tuple:
    """функция принимает строку с полным путем до файла.
    Возвращает кортеж с путем, названием файла и его разрешением"""
    full_path = os.path.dirname(path)
    name = os.path.basename(path)
    path = os.path.splitext(path)
    return full_path, name, path[1]


if __name__ == '__main__':
    print(split_path('C:/Users/text.txt'))