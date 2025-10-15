class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposite(self, amount):
        self.balance += amount
        return self.balance
    
money = BankAccount(1000)
res = money.deposite(200)
print(res)