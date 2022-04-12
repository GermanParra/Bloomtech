from wallet import Wallet
import pytest


# make a fixture to serve as an empty wallet
@pytest.fixture
def empty_wallet():
    '''returns a wallet object with a balance of 0'''
    return Wallet()

# make a fixture to serve as a wallet with $20
@pytest.fixture
def wallet_20():
    '''returns a wallet object with a balance of 20'''
    return Wallet(20)



def test_empty_wallet(empty_wallet):
    '''returns a wallet object with a balance of 0'''
    assert empty_wallet.balance == 0

def test_wallet_20_init(wallet_20):
    '''test wallet init with balance 20 to be 20'''
    assert wallet_20.balance == 20

def test_wallet_20__spend_10(wallet_20):
    '''test wallet with balance 20 then 
       spending 10 to have balance 10'''
    wallet_20.spend_cash(10)
    assert wallet_20.balance == 10

def test_wallet_20__spend_20(wallet_20):
    '''test wallet with balance 20 then 
       spending 20 to have balance 0'''
    wallet_20.spend_cash(20)
    assert wallet_20.balance == 0