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
        print("<" + "=" * 25 + ">")
        print(f"Account id is {self.account_number}")
        print(f"Owners name is {self.name}")
        print(f"Account balance is {self.balance}")
        print("<" + "=" * 25 + ">")


id55665 = BankAccount(55665, "Artemy", 0)
id55666 = BankAccount(55666, "Vildan", 0)
id55667 = BankAccount(55667, "Nikita", 0)

id55665.deposit(4000)
id55666.deposit(13000)
id55667.deposit(5000)

id55665.display()
id55666.display()
id55667.display()