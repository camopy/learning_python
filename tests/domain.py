class User:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


class Bid:
    def __init__(self, user, value):
        self.user = user
        self.value = value


import sys


class Auction:
    def __init__(self, description):
        self.description = description
        self.__bids = []
        self.lowest_bid = sys.float_info.max
        self.highest_bid = sys.float_info.min

    @property
    def bids(self):
        return self.__bids[:]

    def bet(self, bid: Bid):
        self.__bids.append(bid)

        for bid in self.bids:
            if bid.value > self.highest_bid:
                self.highest_bid = bid.value
            if bid.value < self.lowest_bid:
                self.lowest_bid = bid.value
