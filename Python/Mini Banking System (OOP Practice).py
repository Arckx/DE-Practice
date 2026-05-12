class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self._balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(self._balance)
        else:
            print("Negative amount not allowed")

    def withdraw(self, amount):
        if self._balance > 0 and (self._balance - amount) >= 0:
            self._balance -= amount
            print(f"Amount withdrawn: {amount}, Balance remaining: {self._balance}")
        else:
            print("Balance insufficient")
            

class SavingsAccount(BankAccount):
    pass
class CurrentAccount(BankAccount):
    pass

asif = BankAccount(157893, "Asif Haider", 200)
asif.withdraw(50)