class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposite(self, amount):
        new_balance = self.balance + amount
        return new_balance
    
money = BankAccount(1000)
res = money.deposite(200)
print(res)