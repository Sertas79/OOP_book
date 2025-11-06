# Основная программа, контролирующая банк, состоящий из счетов

# Берем весь код класса банка
from Bank import *

# Создаем экземпляр банка
o_bank = Bank()

# Основной код
# создаем два текстовых счета
joes_account_number = o_bank.create_account('Joe', 100, 'JoesPassword')
print('Joe\'s account number is:', joes_account_number)

marys_account_number = o_bank.create_account('Mary', 100, 'MaryPassword')
print('Mary\'s account number is:', marys_account_number)

while True:
    print()
    print('To get an account balance, press b')
    print('To close an account, press c')
    print('To make a deposit, press d')
    print('To open a new account, press o')
    print('To quit, press q')
    print('To show all accounts, press s')
    print('To make a withdrawal, press w')
    print()

    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]
    print()

    if action == 'b':
        o_bank.balance()
    elif action == 'c':
        o_bank.close_account()
    elif action == 'd':
        o_bank.deposit()
    elif action == 'o':
        o_bank.open_account()
    elif action == 's':
        o_bank.show()
    elif action == 'q':
        break
    elif action == 'w':
        o_bank.withdraw()
    else:
        print('Sorry, that was not a valid action. Please try again.')


