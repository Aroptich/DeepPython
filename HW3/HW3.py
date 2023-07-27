# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]
from collections import Counter
from typing import Any


def list_of_repeating_elements(element: list[Any]) -> list[Any]:
    """Функция принимает список элементов.
    Возвращает список повторяющихся элементов"""
    return list(set([el for el in element if element.count(el) > 1]))


# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
# (Может помочь метод translate из модуля string)

def main(text: str, count: int) -> list[tuple[str, int]]:
    """Функция принимает путь к файлу и количество вывода повторений.
    Возвращает список кортежей с повторяющимися элементами"""
    try:
        return Counter(reading_text(text)).most_common(count)
    except Exception as err:
        print(err)


def reading_text(text: str) -> list[str]:
    """Функция принимает путь к файлу.
    Возвращает список слов из файла"""
    try:
        if not isinstance(text, str):
            raise TypeError("Аргумент должен быть строкового типа")
        with open(text, 'r', encoding='utf-8') as file:
            return file.read().lower().split()
    except Exception as err:
        print(err)
        return -1


# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

def backpack(capacity: int) -> dict:
    THINGS = {'яблоко': 0.1,
              'нож': 0.5,
              'коструля': 1.0,
              'ложка': 0.2,
              'вилка': 0.1,
              'картошка': 1.5,
              'спички': 0.05,
              'дрова': 3.0,
              'палатка': 5.0,
              'фонарик': 1.0,
              'мясо': 3.0,
              'аптечка': 1.5}
    cargo = []
    lst_things = []
    for thing in THINGS:
        if THINGS[thing] <= capacity and (sum(cargo) + THINGS[thing]) <= capacity:
            cargo.append(THINGS[thing])
            lst_things.append(thing)
    print(lst_things)





if __name__ == '__main__':
    print(list_of_repeating_elements([1, 2, 3, 1, 2, 4, 5]))
    print(main('text.txt', 10))
    backpack(5)

