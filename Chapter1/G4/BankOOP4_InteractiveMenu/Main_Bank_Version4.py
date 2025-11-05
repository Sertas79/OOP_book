# Интерактивная тестовая программа создания словаря счетов
# Версия 4 с интерактивным меню

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

while True:
    print()
    print('Press b to get th balance')
    print('Press d to make a deposit')
    print('Press o to open a new account')
    print('Press w to make withdrawal')
    print('Press s to show all accounts')
    print('Press q to quit')
    print()

    action = input('What do you want to do? ')
    action = action[0].lower() # захватываем первую букву
    print()

    if action == 'b':
        print('*** Get Balance ***')
        user_account_number = int(input('Please enter the account number: '))
        user_account_password = input('Please enter the account password: ')
        o_account = accounts_dict[user_account_number]
        the_balance = o_account.get_balance(user_account_password)
        if the_balance is not None:
            print('Your balance is:', the_balance)

    elif action == 'd':
        print('*** Deposit ***')
        user_account_number = int(input('Please enter the account number: '))
        user_deposit_amount = int(input('Please enter the amount to deposit: '))
        user_account_password = input('Please enter the account password: ')
        o_account = accounts_dict[user_account_number]
        the_balance = o_account.deposit(user_deposit_amount, user_account_password)
        if the_balance is not None:
            print('Your new balance is:', the_balance)

    elif action == 'o':
        print('*** Open Account ***')
        user_name = input('What is the name for the new user account? ')
        user_starting_amount = int(input('Please enter the starting amount of the account: '))
        user_password = input('Please enter the account password: ')
        o_account = Account(user_name, user_starting_amount, user_password)
        accounts_dict[next_account_number] = o_account
        print('Your  new account number is:', next_account_number)
        next_account_number += 1
        print()

    elif action == 's':
        print('Show:')
        for user_account_number in accounts_dict:
            o_account = accounts_dict[user_account_number]
            print('Account number:', user_account_number)
            o_account.show()

    elif action == 'q':
        break

    elif action == 'w':
        print('*** Withdraw ***')
        user_account_number = int(input('Please enter the account number: '))
        user_withdrawal_amount = int(input('Please enter the amount to deposit: '))
        user_account_password = input('Please enter the account password: ')
        o_account = accounts_dict[user_account_number]
        the_balance = o_account.withdraw(user_withdrawal_amount, user_account_password)
        if the_balance is not None:
            print('Withdrew:', user_withdrawal_amount)
            print('Your new balance is:', the_balance)
    else:
        print('Sorry, that was not a valid action. Please try again.')

    print('Done')

