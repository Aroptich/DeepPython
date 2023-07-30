#Напишите функцию для транспонирования матрицы.
# Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]


def trans_matrix(matrix: list) -> list:
    if valid(matrix):
        new_matrix = [[] for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                new_matrix[j].append(matrix[i][j])
        return new_matrix

def valid(matrix: list) -> bool:
    string_matrix = matrix[0]
    for item in matrix:
        if len(item) != len(string_matrix):
            return False
    return True