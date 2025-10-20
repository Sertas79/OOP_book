# Без ООП
# Банк. Версия 4
# Любое количество счетов- со списками

accountNameList = []
accountBalanceList = []
accountPasswordList = []

def new_account(name, balance, password):
    global accountNameList,accountBalanceList,accountPasswordList
    accountNameList.append(name)
    accountBalanceList.append(balance)
    accountPasswordList.append(password)

def show_account(accountNumber):
    global accountNameList,accountBalanceList,accountPasswordList
    print('Account', accountNumber)
    print('     Name', accountNameList[accountNumber])
    print('     Balance', accountBalanceList[accountNumber])
    print('     Password', accountPasswordList[accountNumber])
    print()


def get_balance(accauntNumber, password):
    global accountNameList,accountBalanceList,accountPasswordList
    if password != accountPasswordList[accauntNumber]:
        print('Wrong password')
        return None
    return accountBalanceList[accauntNumber]

def deposit(accountNumber, amount_to_deposit, password):
    global accountNameList,accountBalanceList,accountPasswordList
    if amount_to_deposit < 0:
        print('You cannot deposit a negative amount!')
        return None

    if password != accountPasswordList[accountNumber]:
        print('Wrong password')
        return None

    accountBalanceList[accountNumber] += amount_to_deposit
    return accountBalanceList[accountNumber]



def withdraw(accountNumber,amount_to_withdraw, password):
    global accountNameList,accountBalanceList,accountPasswordList
    if amount_to_withdraw < 0:
        print('You cannot withdraw a negative amount!')
        return None

    if password != accountPasswordList[accountNumber]:
        print('Wrong password')
        return None

    if amount_to_withdraw > accountBalanceList[accountNumber]:
        print('You cannot withdraw more than your balance!')
        return None

    accountBalanceList[accountNumber] -= amount_to_withdraw
    return accountBalanceList[accountNumber]


print('Joe account is account number:', len(accountNameList))
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





