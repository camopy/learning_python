from tdd.domain import User, Auction, Bid
from tdd.exceptions import InvalidBet

from unittest import TestCase


class TestDealer(TestCase):
    def setUp(self):
        self.amanda = User("Amanda", 500.0)
        self.amanda_bid = Bid(self.amanda, 150.0)
        self.auction = Auction("Notebook")

    def test_should_return_lowest_and_highest_bids_when_added_in_ascending_order(self):
        paulo = User("Paulo", 500.0)
        paulo_bid = Bid(paulo, 100.0)

        self.auction.bet(paulo_bid)
        self.auction.bet(self.amanda_bid)

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

    def test_should_allow_betting_if_auction_is_empty(self):
        self.auction.bet(self.amanda_bid)
        bids_count = len(self.auction.bids)

        self.assertEqual(1, bids_count, "Bet was not accepted")

    def test_should_deny_bet_if_last_bid_is_higher(self):
        self.auction.bet(self.amanda_bid)

        paulo = User("Paulo", 500.0)
        paulo_bid = Bid(paulo, 100.0)

        with self.assertRaises(InvalidBet):
            self.auction.bet(paulo_bid)

    def test_should_deny_bet_if_user_is_the_same_from_last_bid(self):
        self.auction.bet(self.amanda_bid)

        new_bid = Bid(self.amanda, 200.0)

        with self.assertRaises(InvalidBet):
            self.auction.bet(new_bid)
