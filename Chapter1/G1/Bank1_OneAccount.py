# Без ООП
# Банк. Версия 1
# Единственный счет

account0Name = 'Joe'
account0Balance = 100
account0Password = 'soup'

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
        if userPassword != account0Password:
            print('Wrong password')
        else:
            print('Balance: ' + str(account0Balance))
    elif action == 'd':
        print('Make a Deposit')
        userDepositAmount = int(input('Enter your deposit amount: '))
        userPassword = input('Enter your password: ')

        if userDepositAmount < 0:
            print('You cannot make a deposit')
        elif userPassword != account0Password:
            print('Wrong password')
        else:
            account0Balance += userDepositAmount
            print('Your balance: ' + str(account0Balance))
    elif action == 's':
        print('Show account')
        print('     Name', account0Name)
        print('     Balance', account0Balance)
        print('     Password', account0Password)
        print()
    elif action == 'q':
        break
    elif action == 'w':
        print('Make a Withdrawal')
        userWithdrawAmount = int(input('Enter your withdraw amount: '))
        userPassword = input('Enter your password: ')

        if userWithdrawAmount < 0:
            print('You cannot make a withdrawal')
        elif userPassword != account0Password:
            print('Wrong password')
        elif userWithdrawAmount > account0Balance:
            print('You cannot make a withdrawal')
        else:
            account0Balance -= userWithdrawAmount
            print('Your balance: ' + str(account0Balance))


