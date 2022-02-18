class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def __str__(self):
       return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'
    def deposit(self, amount):
        self.balance = self.balance+amount
        print("Deposit Accepted")
    def withdraw(self, amount):
        if(amount>self.balance):
            print("Funds Unavailable!")
        else:
            self.balance = self.balance-amount
            print("Withdrawal Accepted")
        
