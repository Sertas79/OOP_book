# Тестовая программа, использующая счета
# Версия 1, использующая явные переменные для каждого  объекта Account

# Берем весь код из файла класса Account
from Account import *

# создаем два счета
o_joes_account = Account('Joe', 10000, 'JoesPassword')
print('Created an account for Joe')
o_marys_account = Account('Marys', 123456, 'MarysPassword')
print('Created an account for Marys')
o_joes_account.show()
o_marys_account.show()
print()

# вызываем разные методы для разных счетов
print('Calling methods of the two accounts...')
o_joes_account.deposit(50, 'JoesPassword')
o_marys_account.withdraw(345, 'MarysPassword')
o_marys_account.deposit(100, 'MarysPassword')

# отображаем счета
o_joes_account.show()
o_marys_account.show()