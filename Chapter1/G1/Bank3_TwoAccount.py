# Без ООП
# Банк. Версия 3
# Два счета

account0Name = ''
account0Balance = 0
account0Password = ''
account1Name = ''
account1Balance = 0
account1Password = ''
n_accounts = 0

def new_account(account_number, name, balance, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if account_number == 0:
        account0Name = name
        account0Balance = balance
        account0Password = password
    if account_number == 1:
        account1Name = name
        account1Balance = balance
        account1Password = password

def show_account():
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if account0Name != '':
        print('Account 0')
        print('     Name', account0Name)
        print('     Balance', account0Balance)
        print('     Password', account0Password)
        print()
    if account1Name != '':
        print('Account 1')
        print('     Name', account1Name)
        print('     Balance', account1Balance)
        print('     Password', account1Password)
        print()

def get_balance(account_number, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if account_number == 0:
        if password != account0Password:
            print('Wrong password')
            return None
        else:
            return account0Balance

    if account_number == 1:
        if password != account1Password:
            print('Wrong password')
            return None
        else:
            return account1Balance

def deposit(accountNumber, amount_to_deposit, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        if amount_to_deposit < 0:
            print('You cannot deposit a negative amount!')
            return None

        if password != account0Password:
            print('Wrong password')
            return None

        account0Balance += amount_to_deposit
        return account0Balance

    if accountNumber == 1:
        if amount_to_deposit < 0:
            print('You cannot deposit a negative amount!')
            return None

        if password != account1Password:
            print('Wrong password')
            return None

        account1Balance += amount_to_deposit
        return account1Balance

def withdraw(accountNumber,amount_to_withdraw, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        if amount_to_withdraw < 0:
            print('You cannot withdraw a negative amount!')
            return None

        if password != account0Password:
            print('Wrong password')
            return None

        if amount_to_withdraw > account0Balance:
            print('You cannot withdraw more than your balance!')
            return None

        account0Balance -= amount_to_withdraw
        return account0Balance

    if accountNumber == 1:
        if amount_to_withdraw < 0:
            print('You cannot withdraw a negative amount!')
            return None
        if password != account1Password:
            print('Wrong password')
            return None
        account1Balance -= amount_to_withdraw
        return account1Balance

new_account(0, 'Joe', 100, 'soup')
new_account(1,'Nick', 100000, 'jock')


while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print()

    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]
    print()

    if action == 'b':
        print('Get Balance')
        userAccountNumber = int(input('Enter your account number: '))
        userPassword = input('Enter your password: ')
        theBalance = get_balance(userAccountNumber, userPassword)
        if theBalance is not None:
            print('Your balance is', theBalance)
    elif action == 'd':
        print('Make a Deposit')
        userAccountNumber = int(input('Enter your account number: '))
        userDepositAmount = int(input('Enter your deposit amount: '))
        userPassword = input('Enter your password: ')
        newBalance = deposit(userAccountNumber,userDepositAmount, userPassword)
        if newBalance is not None:
            print('Your balance is', newBalance)
    elif action == 'w':
        print('Make a Withdrawal')
        userAccountNumber = int(input('Enter your account number: '))
        userWithdrawAmount = int(input('Enter your withdraw amount: '))
        userPassword = input('Enter your password: ')
        newBalance = withdraw(userAccountNumber,userWithdrawAmount, userPassword)
        if newBalance is not None:
            print('Your balance is', newBalance)
    elif action == 's':
        print('Show account')
        show_account()
    elif action == 'q':
        break

print('Done')





