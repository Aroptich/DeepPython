#Напишите однострочный генератор словаря,который принимает на вход три списка одинаковой длины:
#имена str, ставка int, премия str с указанием процентов вида «10.25%».
#В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
#Сумма рассчитывается как ставка умноженная на процент премии

def bet(names: list[str], bets: list[int], premium: str) -> dict:
    return {name:sum_premium for name, sum_premium in zip(names, [bet + (bet * float(premium)/100) for bet in bets])}

if __name__ == '__main__':
    print(bet(['John', 'Andry', 'Sasha'], [100, 200, 50], '10.25'))