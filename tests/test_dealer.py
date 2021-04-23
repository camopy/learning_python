from domain import User, Auction, Bid
from unittest import TestCase


class TestDealer(TestCase):
    def setUp(self):
        self.amanda = User("Amanda")
        self.amanda_bid = Bid(self.amanda, 150.0)
        self.auction = Auction("Notebook")

    def test_should_return_lowest_and_highest_bids_when_added_in_ascending_order(self):
        paulo = User("Paulo")
        paulo_bid = Bid(paulo, 100.0)

        self.auction.bet(paulo_bid)
        self.auction.bet(self.amanda_bid)

        self.assertEqual(
            self.auction.lowest_bid, paulo_bid.value, "Lowest bid is wrong"
        )
        self.assertEqual(
            self.auction.highest_bid, self.amanda_bid.value, "Highest bid is wrong"
        )

    def test_should_return_lowest_and_highest_bids_when_added_in_descending_order(self):
        paulo = User("Paulo")
        paulo_bid = Bid(paulo, 100.0)

        self.auction.bet(self.amanda_bid)
        self.auction.bet(paulo_bid)

        self.assertEqual(
            self.auction.lowest_bid, paulo_bid.value, "Lowest bid is wrong"
        )
        self.assertEqual(
            self.auction.highest_bid, self.amanda_bid.value, "Highest bid is wrong"
        )

    def test_should_return_lowest_and_highest_bids_when_there_is_only_one_bid(self):
        self.auction.bet(self.amanda_bid)

        self.assertEqual(
            self.auction.lowest_bid, self.amanda_bid.value, "Lowest bid is wrong"
        )
        self.assertEqual(
            self.auction.highest_bid, self.amanda_bid.value, "Highest bid is wrong"
        )
