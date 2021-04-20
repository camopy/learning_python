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

avengers1 = Movie("avengers", 2017, 160)
avengers2 = Movie("avengers", 2018, 160)
avengers3 = Movie("avengers", 2018, 160)

avengers2.addLike()
avengers2.addLike()

friends = Serie("friends", 2010, 10)
friends.addLike()
friends.addLike()
friends.addLike()

weekend_playlist = Playlist("Weekend playlist", [avengers2, friends])
for tvshow in weekend_playlist:
    print(tvshow)

print(f"Playlist size: {len(weekend_playlist)}")

print(avengers1 == avengers2)
print(avengers2 == avengers3)
