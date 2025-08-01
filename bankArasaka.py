class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            print('Введите корректную сумму (число)')
            return

        self.__balance += amount
        print(f'Депозит на сумму {amount} евродолларов пополнен')

    def withdraw(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            print('Введите корректную сумму (число)')
            return

        if self.__balance < amount:
            print('Недостаточно средств на балансе для снятия')
            return

        self.__balance -= amount
        print(f'С баланса снято {amount} евродолларов')

    def get_balance(self):
        print(f'На балансе {self.__balance} евродолларов')


def account_menu():
    account = BankAccount(0)
    menu_option = {
        '1': account.get_balance,
        '2': lambda: account.deposit(input('Введите сумму которую хотите внести на счет: ')),
        '3': lambda: account.withdraw(input('Введите сумму которую хотите снять со счета: ')),
        '4': lambda: print('Выход из программы.') or exit()
    }

    while True:
        enter = input('\nВыбирите действие из списка ниже:'
                      '\n1 - Просмотреть баланс на счете'
                      '\n2 - Внести депозит'
                      '\n3 - Снять наличные'
                      '\n4 - Выйти'
                      '\nНажмите на цифру пункта меню: ')

        action = menu_option.get(enter)
        if action:
            action()
        else:
            print('Неверный ввод')


account_menu()
