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

    def bank_fees(self):
        self.balance *= 0.95

    def display(self):
        print(f"Account id is {self.account_number}")
        print(f"Owners name is {self.name}")
        print(f"Account balance is {self.balance}")
