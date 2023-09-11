import csv
import random


def gen_csv() -> None:
    """Создание файла csv с быллами и оценками"""
    with open('lessons_and_grades.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        lessons = ['mathematics', 'physics', 'history', 'english', 'biology', 'chemistry']
        filewriter.writerow(['Lessons', 'Mark', 'Test_result'])
        for item in range(len(lessons)):
            mark = random.randint(2, 6)
            if mark == 2:
                test_result = random.randint(0, 25)
            elif mark == 3:
                test_result = random.randint(25, 50)
            elif mark == 4:
                test_result = random.randint(50, 90)
            else:
                test_result = random.randint(90, 101)
            filewriter.writerow([lessons[item], mark, test_result])

class Csv():
    marks_and_tests_results = gen_csv()

    def lessons_csv(self):
        '''Возвращает список предметов'''
        with open('lessons_and_grades.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            lessons = [row['Lessons'] for row in reader]
        return lessons

    def marks_csv(self)-> list[str]:
        """Возвращает список оценок по предметам"""
        with open('lessons_and_grades.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            marks = [int(row['Mark']) for row in reader]
        return marks

    def test_results_csv(self):
        with open('lessons_and_grades.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            test_results = [int(row['Test_result']) for row in reader]
        return test_results
