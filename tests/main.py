from domain import Auction, User, Bid

paulo = User("Paulo")
amanda = User("Amanda")

paulo_bid = Bid(paulo, 100.0)
amanda_bid = Bid(amanda, 150.0)

auction = Auction("Notebook")

auction.bet(paulo_bid)
auction.bet(amanda_bid)

for bid in auction.bids:
    print(f"{bid.user.name.title()} has bet {bid.value}")

print(f"Highest bid: {auction.highest_bid}")
print(f"Lowest bid: {auction.lowest_bid}")
