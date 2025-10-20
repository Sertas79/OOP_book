# Без ООП
# Банк. Версия 5
# Любое количество счетов- со списком словарей

accountList = []

def new_account(a_name, a_balance, a_password):
    global accountList
    newAccountDict = {'name': a_name, 'balance': a_balance, 'password': a_password}
    accountList.append(newAccountDict)

def show_account(accountNumber):
    global accountList
    print('Account', accountNumber)
    thisAccountDict = accountList[accountNumber]
    print('     Name', thisAccountDict['name'])
    print('     Balance', thisAccountDict['balance'])
    print('     Password', thisAccountDict['password'])
    print()


def get_balance(accountNumber, password):
    global accountList
    thisAccountDict = accountList[accountNumber]
    if password != thisAccountDict['password']:
        print('Wrong password')
        return None
    return thisAccountDict['balance']

def deposit(accountNumber, amount_to_deposit, password):
    global accountList
    thisAccountDict = accountList[accountNumber]
    if amount_to_deposit < 0:
        print('You cannot deposit a negative amount!')
        return None

    if password != thisAccountDict['password']:
        print('Wrong password')
        return None

    thisAccountDict['balance'] += amount_to_deposit
    return thisAccountDict['balance']



def withdraw(accountNumber,amount_to_withdraw, password):
    global accountList
    thisAccountDict = accountList[accountNumber]
    if amount_to_withdraw < 0:
        print('You cannot withdraw a negative amount!')
        return None

    if password != thisAccountDict['password']:
        print('Wrong password')
        return None

    if amount_to_withdraw > thisAccountDict['balance']:
        print('You cannot withdraw more than your balance!')
        return None

    thisAccountDict['balance'] -= amount_to_withdraw
    return thisAccountDict['balance']


print('Joe account is account number:', len(accountList))
new_account('Joe', 100, 'soup')
new_account('Nick', 100000, 'jock')


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
        userAccountNumber = int(input('Enter your account number: '))
        print('Show account')
        show_account(userAccountNumber)
    elif action == 'q':
        break

print('Done')





