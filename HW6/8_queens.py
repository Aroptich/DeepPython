# Функция для проверки, угрожают ли два ферзя друг другу или нет
def isSafe(mat, r, c):
    # возвращает false, если два ферзя используют один и тот же столбец.
    for i in range(r):
        if mat[i][c] == 'Q':
            return False

    # возвращает false, если два ферзя делят одну и ту же `диагональ`.
    (i, j) = (r, c)
    while i >= 0 and j >= 0:
        if mat[i][j] == 'Q':
            return False
        i = i - 1
        j = j - 1

    # возвращает false, если два ферзя делят одну и ту же диагональ `/`
    (i, j) = (r, c)
    while i >= 0 and j < len(mat):
        if mat[i][j] == 'Q':
            return False
        i = i - 1
        j = j + 1

    return True


def printSolution(mat):
    for r in mat:
        print(str(r).replace(',', '').replace('\'', ''))
    print()


def nQueen(mat, r):
    # , если N ферзей расставлены успешно, вывести решение
    if r == len(mat):
        printSolution(mat)
        return

    # поместите ферзя на каждую клетку в текущем ряду `r`
    # и повторяться для каждого действительного движения
    for i in range(len(mat)):

        # , если никакие два ферзя не угрожают друг другу
        if isSafe(mat, r, i):
            # поставить ферзя на текущую клетку
            mat[r][i] = 'Q'

            # повторяется для следующей строки
            nQueen(mat, r + 1)

            # вернуться и убрать ферзя с текущего поля
            mat[r][i] = 0


if __name__ == '__main__':
    # `N × N` шахматная доска
    N = 8

    # `mat[][]` отслеживает положение ферзей в
    # текущая конфигурация
    mat = [[0 for x in range(N)] for y in range(N)]

    nQueen(mat, 0)