from tdd.domain import User, Auction

import pytest


@pytest.fixture
def paulo():
    return User("Paulo", 500.0)


@pytest.fixture
def auction():
    return Auction("Notebook")


def test_should_substract_value_from_user_wallet_when_bidding(paulo, auction):
    paulo.bet(auction, 50.0)
    assert paulo.wallet == 450.0


def test_should_allow_betting_if_value_is_lower_than_wallet(paulo, auction):
    paulo.bet(auction, 50.0)
    assert paulo.wallet == 450.0


def test_should_allow_betting_if_value_is_equal_wallet(paulo, auction):
    paulo.bet(auction, 500.0)
    assert paulo.wallet == 0.0


def test_should_deny_betting_if_value_is_higher_than_wallet(paulo, auction):
    with pytest.raises(ValueError):
        paulo.bet(auction, 600.0)