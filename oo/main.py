from account import Account

account = Account(123, "Paulo", 100, 1000)

print("Balance: ", account.balance)

account.deposit(50)
print("Balance: ", account.balance)

account.whitdraw(20)
print("Balance: ", account.balance)