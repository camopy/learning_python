from account import Account
from movie import Movie
from serie import Serie
from playlist import Playlist

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
avengers.addLike()
avengers.addLike()

friends = Serie("friends", 2010, 10)
friends.addLike()
friends.addLike()
friends.addLike()

weekend_playlist = Playlist("Weekend playlist", [avengers, friends])
for tvshow in weekend_playlist:
    print(tvshow)

print(f"Playlist size: {len(weekend_playlist)}")
