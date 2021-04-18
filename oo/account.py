class Account:
    bank_code = "001"

    def __init__(self, number, owner, balance, limit):
        self.__number = number
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit

    def whitdraw(self, amount):
        if self.__validWhitdraw(amount):
            self.__balance -= amount
        else:
            print("Not enough funds")

    def deposit(self, amount):
        self.__balance += amount

    def transfer(self, amount, account):
        self.whitdraw(amount)
        account.deposit(amount)

    @property
    def number(self):
        return self.__number

    @property
    def owner(self):
        return self.__owner

    @property
    def balance(self):
        return self.__balance

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        self.__limit = limit

    def __validWhitdraw(self, amount):
        available_amount = self.__balance + self.__limit
        return available_amount > amount

    @staticmethod
    def bank_codes():
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}
