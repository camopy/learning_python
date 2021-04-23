from tdd.domain import User, Auction


def test_should_substract_value_fromj_user_wallet_when_bidding():
    paulo = User("Paulo", 500.0)

    auction = Auction("Notebook")

    paulo.bet(auction, 50.0)

    assert paulo.wallet == 450.0