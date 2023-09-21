import pytest

from DeepPython.HW14.discriptors import Сhecking_the_value_Descriptor


def test_integer_float1():
    assert Сhecking_the_value_Descriptor.integer_float(6) == None


def test_integer_float2():
    assert Сhecking_the_value_Descriptor.integer_float(6.7) == None


def test_integer_float3():
    with pytest.raises(TypeError) as err:
        Сhecking_the_value_Descriptor.integer_float('6')
    assert 'Значения длины стороны должны быть целымили вещественным числом!' == err.value.args[0]


def test_positive_value1():
    with pytest.raises(TypeError) as err:
        Сhecking_the_value_Descriptor.positive_value(0)
    assert "Значение должно быть положительным!" == err.value.args[0]


def test_positive_value2():
    with pytest.raises(TypeError) as err:
        Сhecking_the_value_Descriptor.positive_value(-1)
    assert "Значение должно быть положительным!" == err.value.args[0]


def test_positive_value3():
    with pytest.raises(TypeError) as err:
        Сhecking_the_value_Descriptor.positive_value('-1')
    assert "Значение должно быть положительным!" == err.value.args[0]


def test_positive_value4():
    assert Сhecking_the_value_Descriptor.positive_value(5) == 5


def test_positive_value5():
    assert Сhecking_the_value_Descriptor.positive_value(6.5) == 6.5


if __name__ == '__main__':
    pytest.main()
