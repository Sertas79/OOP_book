# Тестовая программа, использующая счета
# Версия 3 с использованием словаря счетов

# Берем весь код из файла класса Account
from Account import *
accounts_dict = {}
next_account_number = 0

# создаем два счета
o_account = Account('Joe', 100, 'JoesPassword')
joes_account_number = next_account_number
accounts_dict[joes_account_number] = o_account
print('Account number for Joe is:', joes_account_number)
next_account_number += 1

o_account = Account('Mary', 12345, 'MarysPassword')
myrys_account_number = next_account_number
accounts_dict[myrys_account_number] = o_account
print('Account number for Marys is:', myrys_account_number)
next_account_number += 1

accounts_dict[joes_account_number].show()
accounts_dict[myrys_account_number].show()
print()

# вызываем разные методы для разных счетов
print('Calling method if the two accounts...')
accounts_dict[joes_account_number].deposit(50, 'JoesPassword')
accounts_dict[myrys_account_number].withdraw(345, 'MaryPassword')
accounts_dict[myrys_account_number].deposit(100, 'MaryPassword')

# отображаем счета
accounts_dict[joes_account_number].show()
accounts_dict[myrys_account_number].show()

# создаем новый счет с информацией от пользователя
print()
user_name = input('What us the name for the new user account? ')
user_balance = int(input('What is the balance for the new user account? '))

