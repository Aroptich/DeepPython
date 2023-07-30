#Создайте функцию генератор чисел Фибоначчи
def febonacci(number: int):
    if number in (1,2):
        return 1
    return febonacci(number - 1) + febonacci(number - 2)


if __name__ == '__main__':
    print(febonacci(6))