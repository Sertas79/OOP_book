# Класс счета

class Account:
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password

    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print('Password does not match')
            return None

        if amountToDeposit < 0:
            print('Amount cannot be negative')
            return None

        self.balance += amountToDeposit
        return self.balance

    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print('Password does not match')
            return None

        if amountToWithdraw < 0:
            print('Amount cannot be negative')
            return None

        self.balance -= amountToWithdraw
        return self.balance

    def show(self):
        print('     Name: ', self.name)
        print('     Balance: ', self.balance)
        print('     Password: ', self.password)
        print()

    def get_balance(self, password):
        if password != self.password:
            print('Password does not match')
            return None
        return self.balance
