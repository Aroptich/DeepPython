class ATM:
    '''Класс банкомат'''
    BALANCE = 0
    __counter = 0
    operations = []

    def deposit_money(self, money: int):
        '''Функция позволяет пополнить счет'''
        if money % 50 == 0:
            self.BALANCE += money
            self.__luxury_tax()
            self.__counter += 1
            self.__interest_on_deposit()
            self.operations.append(self.BALANCE)
        print(f'Счет пополнен на {money} у.е\n'
              f'Ваш баланс {self.BALANCE} у.е')
    def withdraw_money(self, money: int):
        if money <= self.BALANCE:
            if (self.BALANCE - (money + self.__withdrawal_percentage(money))) > 0:
                self.BALANCE -= money + self.__withdrawal_percentage(money)
                self.__counter += 1
                self.__interest_on_deposit()
                self.operations.append(self.BALANCE)
                print(f"Сумма для снятия {money} у.е\n"
                      f"Коммисия за снятие составит: {self.__withdrawal_percentage(money)} у.е\n"
                      f"Ваш баланс {self.BALANCE} у.е")
            else:
                print(f'Недостаточно средств на счете!\n'
                      f'Введите другую сумму')

        else:
            print(f'Недостаточно средст на счете!\n'
                  f'Выберите другую сумму')

    def __luxury_tax(self):
        """Налог на роскошь"""
        limit = 5_000_000
        if self.BALANCE >= limit:
            self.BALANCE -= self.BALANCE*0.1
            print(f'Ваш налог на роскошь составит: {self.BALANCE*0.1} у.е')

    def __withdrawal_percentage(self, money: int) -> int:
        """Функция получает на вход сумму для снятия наличных.
        Возвращает сумму коммисии"""
        if money % 50 == 0:
            if (money * 1.5) // 100 < 30:
                money_percent = 30
                return money_percent
            elif money * 1.5 // 100 > 30:
                money_percent = money * 1.5 // 100
                return money_percent
            elif (money * 1.5) // 100 >= 600:
                money_percent = 600
                return money_percent
        else:
            print(f'Сумма не кратна 50!\n'
                  f'Введите сумму кратную 50\n'
                  f'Ваш баланс {self.BALANCE} у.е')


    def exit_of_atm(self):
        """Функция выполняет выход конец операций со счетом"""
        quit_of_atm = input('Для подтверждения выхода введите y/n: ')
        if quit_of_atm == 'y':
            print('Выход из системы выполнен')
    def __interest_on_deposit(self):
        """Функция начисляет процент от влада"""
        if self.__counter % 3 ==0:
            deposit_percentage = 0.03
            self.BALANCE += self.BALANCE*deposit_percentage
            print(f'Процент от влада составил: {self.BALANCE*deposit_percentage} у.е')



if __name__ == '__main__':
    a = ATM()
    a.deposit_money(100)
    a.deposit_money(100)
    a.deposit_money(100)
    a.withdraw_money(50)
    a.withdraw_money(50)
    a.withdraw_money(50)
    print(a.operations)


