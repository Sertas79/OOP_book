# Тестовая программа, использующая счета
# Версия 2, с использованием списка счетов

# Берем весь код из файла класса Account
from Account import *

# начинаем с пустого списка
account_list = []

# создаем два счета
o_account = Account('Joe', 100, 'JoesPassword')
account_list.append(o_account)
print('Joe`s account number is 0')

o_account = Account('Mary', 12345, 'MarysPassword')
account_list.append(o_account)
print('Mary`s account number is 1')

account_list[0].show()
account_list[1].show()
print()

# вызываем разные методы для разных счетов
print('Calling methods of the two accounts ...')
account_list[0].deposit(50, 'JoesPassword')
account_list[1].withdraw(345, 'MarysPassword')
account_list[1].deposit(100, 'MarysPassword')

# отображаем счет
account_list[0].show()
account_list[1].show()

# создаем новый счет с информацией от пользователей
print()
user_name = input('Enter your name: ')
user_balance = int(input('Enter your balance: '))
user_password = input('Enter your password: ')
o_account = Account(user_name, user_balance, user_password)
account_list.append(o_account)

# отображаем вновь созданный счет пользователя
print('Create new account, account number is 2')
account_list[2].show()

# вносим 100 на новый счет
account_list[2].deposit(100, user_password)
user_balance = account_list[2].get_balance(user_password)
print()
print('After depositing 100, the user`s balance is', user_balance)

# отображаем новый счет
account_list[2].show