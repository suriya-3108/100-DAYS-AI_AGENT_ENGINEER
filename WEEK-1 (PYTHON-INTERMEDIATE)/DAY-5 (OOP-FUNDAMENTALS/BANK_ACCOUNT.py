"""Question 2 — Bank Account (Constructor + Methods)
Create a class BankAccount.
Requirements:

Attributes:
account_holder
balance

Methods:
deposit(amount)
withdraw(amount)
check_balance()"""


class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount 
        print("Deposit success")
        print(f"New balance is: {self.balance}")
        
    def withdraw(self, amount):
        if self.balance < amount:
            print(f"insufficient balance!!!")
        else:
            self.balance -= amount
            print(f"the withdrwal amount is: {amount}")
            print(f"the new balance is: {self.balance}")
    
    def check_balance(self):
        print(f"the balance is: {self.balance}")

b = BankAccount('suriya',1000)

b.deposit(200)

b.withdraw(500)

b.check_balance()