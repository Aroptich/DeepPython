from discriptors import Сhecking_the_value_Descriptor


class Triangle:
    __slots__ = ('_side_a', '_side_b', '_side_c')
    side_a = Сhecking_the_value_Descriptor()
    side_b = Сhecking_the_value_Descriptor()
    side_c = Сhecking_the_value_Descriptor()

    def __init__(self, side_a: (int, float), side_b: (int, float), side_c: (int, float)):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def equal_sides(self) -> bool:
        """Функция возвращает True(если все стороны равны) или False(если стороны не равны)"""
        return self.side_a == self.side_b == self.side_c

    @property
    def two_equal_sides(self) -> bool:
        """Функция возвращает True(если 2 стороны равны)"""
        return (self.side_a == self.side_b) or (self.side_b == self.side_c) or (self.side_a == self.side_c)

    def __repr__(self):
        return f'Сторона "a" - {self.side_a}\n' \
               f'Сторона "b" - {self.side_b}\n' \
               f'Сторона "c" - {self.side_c}'


if __name__ == '__main__':
    a = Triangle(1, 1, 1)
    print(a.equal_sides())
