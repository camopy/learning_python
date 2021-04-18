class Account:
    def __init__(self, number, owner, balance, limit):
        self.__number = number
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit

    def whitdraw(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    def transfer(self, amount, account):
        self.whitdraw(amount)
        account.deposit(amount)
