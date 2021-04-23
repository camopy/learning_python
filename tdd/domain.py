class User:
    def __init__(self, name, wallet):
        self.__name = name
        self.__wallet = wallet

    @property
    def name(self):
        return self.__name

    @property
    def wallet(self):
        return self.__wallet

    def bet(self, auction, value):
        if self._valid_value(value):
            bid = Bid(self, value)
            auction.bet(bid)
            self.__wallet -= value
        else:
            raise ValueError("Bet is higher than wallet")

    def _valid_value(self, value):
        return value <= self.wallet


class Bid:
    def __init__(self, user, value):
        self.user = user
        self.value = value


class Auction:
    def __init__(self, description):
        self.description = description
        self.__bids = []
        self.lowest_bid = 0
        self.highest_bid = 0

    @property
    def bids(self):
        return self.__bids[:]

    def bet(self, bid: Bid):
        if self.validate_bid(bid):
            if not self._has_bids():
                self.lowest_bid = bid.value
            self.highest_bid = bid.value

            self.__bids.append(bid)

    def validate_bid(self, bid: Bid):
        if self._has_bids():
            if self._same_user_from_last_bid(bid):
                raise ValueError("User cannot not be the same from last bid")
            elif self._higher_bid_than_last_bid(bid):
                raise ValueError("Bid value must be higher than last bid")

        return True

    def _has_bids(self):
        return self.bids

    def _same_user_from_last_bid(self, bid):
        if self._has_bids():
            return self.bids[-1].user == bid.user
        return False

    def _higher_bid_than_last_bid(self, bid):
        if self._has_bids():
            return self.bids[-1].value > bid.value
        return False
