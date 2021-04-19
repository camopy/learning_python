from account import Account
from movie import Movie
from serie import Serie

# account = Account(123, "Paulo", 100, 1000)

# print(account.owner)

# print("Balance: ", account.balance)

# account.deposit(50)
# print("Balance: ", account.balance)

# account.whitdraw(20)
# print("Balance: ", account.balance)

# account.whitdraw(1300)
# print("Balance: ", account.balance)

# print(Account.bank_code)
# print(Account.bank_codes())

avengers = Movie("avengers", 2018, 160)
# print(avengers.name)
avengers.addLike()
avengers.addLike()
# print(avengers.duration)
# print(avengers.likes)

friends = Serie("friends", 2010, 10)
# print(friends.name)
friends.addLike()
friends.addLike()
friends.addLike()
# print(friends.seasons)
# print(friends.likes)

playlist = [avengers, friends]
for tvshow in playlist:
    print(tvshow)