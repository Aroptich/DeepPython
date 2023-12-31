class TriangleError(Exception):
    """Выбрасывается исключение, когда невозможно построить правильный треугольник"""
    pass


class MatrixError(Exception):
    """Выбрасывает исключение, когда невозможно произвести транспонирование матриц"""
    pass


class RectangleError(Exception):
    """Выбрасывается исключение, когда одна из сторон меньше либо равна нуля"""
    pass
