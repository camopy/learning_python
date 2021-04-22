from domain import User, Auction, Bid, Dealer
from unittest import TestCase


class TestDealer(TestCase):
    def setUp(self):
        self.amanda = User("Amanda")
        self.amanda_bid = Bid(self.amanda, 150.0)
        self.auction = Auction("Notebook")
        self.dealer = Dealer()

    def test_should_return_lowest_and_highest_bids_when_added_in_ascending_order(self):
        paulo = User("Paulo")
        paulo_bid = Bid(paulo, 100.0)

        self.auction.bids.append(paulo_bid)
        self.auction.bids.append(self.amanda_bid)

        self.dealer.check(self.auction)

        self.assertEqual(self.dealer.lowest_bid, paulo_bid.value, "Lowest bid is wrong")
        self.assertEqual(
            self.dealer.highest_bid, self.amanda_bid.value, "Highest bid is wrong"
        )

    def test_should_return_lowest_and_highest_bids_when_added_in_descending_order(self):
        paulo = User("Paulo")
        paulo_bid = Bid(paulo, 100.0)

        self.auction.bids.append(self.amanda_bid)
        self.auction.bids.append(paulo_bid)

        self.dealer.check(self.auction)

        self.assertEqual(self.dealer.lowest_bid, paulo_bid.value, "Lowest bid is wrong")
        self.assertEqual(
            self.dealer.highest_bid, self.amanda_bid.value, "Highest bid is wrong"
        )

    def test_should_return_lowest_and_highest_bids_when_there_is_only_one_bid(self):
        self.auction.bids.append(self.amanda_bid)

        self.dealer.check(self.auction)

        self.assertEqual(
            self.dealer.lowest_bid, self.amanda_bid.value, "Lowest bid is wrong"
        )
        self.assertEqual(
            self.dealer.highest_bid, self.amanda_bid.value, "Highest bid is wrong"
        )
