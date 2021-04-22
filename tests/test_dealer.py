from domain import User, Auction, Bid, Dealer
from unittest import TestCase


class TestDealer(TestCase):
    def test_check(self):
        paulo = User("Paulo")
        amanda = User("Amanda")

        paulo_bid = Bid(paulo, 100.0)
        amanda_bid = Bid(amanda, 150.0)

        auction = Auction("Notebook")

        auction.bids.append(paulo_bid)
        auction.bids.append(amanda_bid)

        dealer = Dealer()
        dealer.check(auction)

        self.assertEqual(dealer.lowest_bid, paulo_bid.value, "Lowest bid is wrong")
        self.assertEqual(dealer.highest_bid, amanda_bid.value, "Highest bid is wrong")