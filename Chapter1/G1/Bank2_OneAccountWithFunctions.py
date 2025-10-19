# Без ООП
# Банк. Версия 2
# Единственный счет

accountName = ''
accountBalance = 0
accountPassword = ''

def new_account(name, balance, password):
    global accountName, accountBalance, accountPassword
    accountName = name
    accountBalance = balance
    accountPassword = password

def show_account():
    global accountName, accountBalance, accountPassword
    print('     Name', accountName)
    print('     Balance', accountBalance)
    print('     Password', accountPassword)
    print()

def get_balance(password):
    global accountName, accountBalance, accountPassword
    if password != accountPassword:
        print('Wrong password')
        return None
    else:
        return accountBalance

def deposit(amount_to_deposit, password):
    global accountName, accountBalance, accountPassword
    if amount_to_deposit < 0:
        print('You cannot deposit a negative amount!')
        return None

    if password != accountPassword:
        print('Wrong password')
        return None

    accountBalance += amount_to_deposit
    return accountBalance

def withdraw(amount_to_withdraw, password):
    global accountName, accountBalance, accountPassword
    if amount_to_withdraw < 0:
        print('You cannot withdraw a negative amount!')
        return None

    if password != accountPassword:
        print('Wrong password')
        return None

    if amount_to_withdraw > accountBalance:
        print('You cannot withdraw more than your balance!')
        return None

    accountBalance -= amount_to_withdraw
    return accountBalance

new_account('Joe', 100, 'soup')

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
        userPassword = input('Enter your password: ')
        theBalance = get_balance(userPassword)
        if theBalance is not None:
            print('Your balance is', theBalance)
    elif action == 'd':
        print('Make a Deposit')
        userDepositAmount = int(input('Enter your deposit amount: '))
        userPassword = input('Enter your password: ')
        newBalance = deposit(userDepositAmount, userPassword)
        if newBalance is not None:
            print('Your balance is', newBalance)
    elif action == 'w':
        print('Make a Withdrawal')
        userWithdrawAmount = int(input('Enter your withdraw amount: '))
        userPassword = input('Enter your password: ')
        newBalance = withdraw(userWithdrawAmount, userPassword)
        if newBalance is not None:
            print('Your balance is', newBalance)
    elif action == 's':
        print('Show account')
        show_account()
    elif action == 'q':
        break





