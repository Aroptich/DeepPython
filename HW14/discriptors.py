class Сhecking_the_value_Descriptor:

    @classmethod
    def integer_float(cls, value: (int, float)) -> None:
        """
        Функция проверяет значение на его тип
        >>> integer_float(3)
        None
        >>> integer_float(5.6)
        None
        :param value: аргумент(целое или вещественное число)
        :return: None
        """
        if not isinstance(value, (int, float)):
            raise TypeError('Значения длины стороны должны быть целымили вещественным числом!')

    @classmethod
    def positive_value(cls, value: (int, float)) -> (int, float):
        """
        Функция проверяет значение является ли оно положительным и возвращает значение или исключение
        >>> positive_value(5)
        4
        >>> positive_value(6.3)
        6.3
        :param value: аргумент(вещественное или целое число)
        :return: value
        """
        if not isinstance(value, (int, float)) or value <= 0:
            raise TypeError("Значение должно быть положительным!")
        else:
            return value

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        value = self.integer_float(value)
        self.positive_value(value)
        setattr(instance, self.name, value)




