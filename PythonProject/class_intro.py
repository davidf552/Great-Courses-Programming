from datetime import date
class BankAccount:
    def __init__(self, initial_amount = 0.0):
        self._deposits = []
        self._balance = initial_amount
        self.opendate = date(2025, 3,30)
    def makeDeposit(self,amount):
        self._balance += amount
        self._deposits.append(amount)
    def makeWithdrawal(self,amount):
        self._balance -= amount
    def getBalance(self):
        return self._balance
    def getDeposits(self):
        copied_list = self._deposits[:]
        return copied_list
checking_account = BankAccount(100.00)
checking_account.makeDeposit(50.00)
print(checking_account.getBalance())
print(checking_account.getDeposits())