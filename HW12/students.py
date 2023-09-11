from discripters import Last_name
from gen_csv import Csv

class Student_class:
    __slots__ = ('_name', '_second_name', '_last_name')
    name = Last_name()
    second_name = Last_name()
    last_name = Last_name()

    def __init__(self, name: str, second_name: str, last_name: str):
        self.name = name
        self.second_name = second_name
        self.last_name = last_name

    def average_test_score(self):
        """Возвращает средний балл за тесты по предметам"""
        result = Csv.test_results_csv(self)
        return f'Средний балл за тесты по предмета: {round(sum(result)/len(result), 2)}'

    def average_score_in_subjects(self):
        """Возвращает среднюю оценку по предметам"""
        result = Csv.marks_csv(self)
        return f'Средняя оценка по предметам: {round(sum(result)/len(result), 2)}'

student = Student_class('Иван', 'Иванович', 'Иванов')
print(student.average_test_score())
print(student.average_score_in_subjects())

