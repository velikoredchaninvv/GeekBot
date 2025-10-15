class BankAccout:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return('Недостаточно средств на счёте')
    
    def get_balance(self):
        return self.balance

money = BankAccout(100)
money.deposit(100)
money.withdraw(30)
print(money.get_balance())