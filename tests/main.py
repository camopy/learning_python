from domain import Auction, User, Bid, Dealer

paulo = User("Paulo")
amanda = User("Amanda")

paulo_bid = Bid(paulo, 100.0)
amanda_bid = Bid(amanda, 150.0)

auction = Auction("Notebook")

auction.bids.append(paulo_bid)
auction.bids.append(amanda_bid)

for bid in auction.bids:
    print(f"{bid.user.name.title()} has bet {bid.value}")

dealer = Dealer()
dealer.check(auction)

print(f"Highest bid: {dealer.highest_bid}")
print(f"Lowest bid: {dealer.lowest_bid}")
