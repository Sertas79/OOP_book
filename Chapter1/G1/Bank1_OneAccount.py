# Без ООП
# Банк. Версия 1
# Единственный счет

accountName = 'Joe'
accountBalance = 100
accountPassword = 'soup'

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
        if userPassword != accountPassword:
            print('Wrong password')
        else:
            print('Balance: ' + str(accountBalance))
    elif action == 'd':
        print('Make a Deposit')
        userDepositAmount = int(input('Enter your deposit amount: '))
        userPassword = input('Enter your password: ')

        if userDepositAmount < 0:
            print('You cannot make a deposit')
        elif userPassword != accountPassword:
            print('Wrong password')
        else:
            accountBalance += userDepositAmount
            print('Your balance: ' + str(accountBalance))
    elif action == 's':
        print('Show account')
        print('     Name', accountName)
        print('     Balance', accountBalance)
        print('     Password', accountPassword)
        print()
    elif action == 'q':
        break
    elif action == 'w':
        print('Make a Withdrawal')
        userWithdrawAmount = int(input('Enter your withdraw amount: '))
        userPassword = input('Enter your password: ')

        if userWithdrawAmount < 0:
            print('You cannot make a withdrawal')
        elif userPassword != accountPassword:
            print('Wrong password')
        elif userWithdrawAmount > accountBalance:
            print('You cannot make a withdrawal')
        else:
            accountBalance -= userWithdrawAmount
            print('Your balance: ' + str(accountBalance))


