# Банк, управляющий словарем объектов Account
from Account import *

class Bank:
    def __init__(self):
        self.accounts_dict = {}
        self.next_accounts_number = 0

    def create_account(self, the_name, the_balance, the_password):
        o_account = Account(the_name, the_balance, the_password)
        new_account_number = self.next_accounts_number
        self.accounts_dict[new_account_number] = o_account
        # увеличиваем на единицу для подготовки к созданию следующей
        # учетной записи
        self.next_accounts_number += 1
        return new_account_number

    def open_account(self):
        print('*** Open Account ***')
        user_name = input('What is the name for the new user account? ')
        user_starting_amount = int(input('Please enter the starting amount of the account: '))
        user_password = input('Please enter the account password: ')
        account_number = self.create_account(user_name, user_starting_amount, user_password)
        print('You new account number is:', account_number)
        print()

    def close_account(self):
        print('*** Close Account ***')
        user_account_number = int(input('What is your account number? '))
        user_password = input('Please enter the account password: ')
        o_account = self.accounts_dict[user_account_number]
        the_balance = o_account.get_balance(user_password)
        if the_balance is not None:
            print('You had', the_balance, 'in your account, which is'
                                          'being returned to you.')
            # удаляем учетную запись пользователя из словаря учетных
            # записей
            del self.accounts_dict[user_account_number]
            print('Your account is now closed.')

    def balance(self):
        print('*** Get Balance ***')
        user_account_number = int(input('What is your account number? '))
        user_password = input('Please enter the account password: ')
        o_account = self.accounts_dict[user_account_number]
        the_balance = o_account.get_balance(user_password)
        if the_balance is not None:
            print('Your balance is:', the_balance)

    def deposit(self):
        print('*** Deposit ***')
        account_num = int(input('What is your account number? '))
        deposit_amount = int(input('Please enter the amount you want to deposit: '))
        user_account_password = input('Please enter the account password: ')
        o_account = self.accounts_dict[account_num]
        the_balance = o_account.deposit(deposit_amount, user_account_password)
        if the_balance is not None:
            print('Your balance is:', the_balance)

    def show(self):
        print('*** Show ***')
        for user_account_number in self.accounts_dict:
            o_account = self.accounts_dict[user_account_number]
            print('Account:', user_account_number)
            o_account.show()

    def withdraw(self):
        print('*** Withdraw ***')
        user_account_number = int(input('What is your account number? '))
        user_amount = int(input('Please enter the amount you want to withdraw: '))
        user_account_password = input('Please enter the account password: ')
        o_account = self.accounts_dict[user_account_number]
        the_balance = o_account.withdraw(user_amount, user_account_password)
        if the_balance is not None:
            print('Withdrew:', user_amount)
            print('Your balance is:', the_balance)

