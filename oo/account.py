class Account:
    def __init__(self, number, owner, balance, limit):
        self.number = number
        self.owner = owner
        self.balance = balance
        self.limit = limit

    def whitdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance
