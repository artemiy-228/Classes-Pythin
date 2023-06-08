class BankAccount:

    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, dep):
        self.balance += dep

    def withdraw(self, money):
        if money <= self.balance:
            self.balance -= money
        else:
            print("not enough balance")

