from unittest import TestCase, main
import doctest

from DeepPython.HW14.discriptors import Сhecking_the_value_Descriptor

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(Сhecking_the_value_Descriptor))
    return tests
class Test_discriptors(TestCase):
    def test_integer_float1(self):
        self.assertEqual(Сhecking_the_value_Descriptor.integer_float(2), None)

    def test_integer_float2(self):
        self.assertEqual(Сhecking_the_value_Descriptor.integer_float(3.5), None)

    def test_integer_float3(self):
        with self.assertRaises(TypeError) as err:
            Сhecking_the_value_Descriptor.integer_float('2')
        self.assertEqual('Значения длины стороны должны быть целымили вещественным числом!', err.exception.args[0])

    def test_positive_value1(self):
        with self.assertRaises(TypeError) as err:
            Сhecking_the_value_Descriptor.positive_value(0)
        self.assertEqual("Значение должно быть положительным!", err.exception.args[0])

    def test_positive_value2(self):
        with self.assertRaises(TypeError) as err:
            Сhecking_the_value_Descriptor.positive_value(-1)
        self.assertEqual("Значение должно быть положительным!", err.exception.args[0])

    def test_positive_value3(self):
        with self.assertRaises(TypeError) as err:
            Сhecking_the_value_Descriptor.positive_value('-1')
        self.assertEqual('Значение должно быть положительным!', err.exception.args[0])

    def test_positive_value4(self):
        self.assertEqual(Сhecking_the_value_Descriptor.positive_value(5),5)

    def test_positive_value5(self):
        self.assertEqual(Сhecking_the_value_Descriptor.positive_value(3.6), 3.6)


if __name__ == '__main__':
    main()
