from brownie import FundMe, network, config
from brownie.network import account
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    withdraw = FundMe[-1]
    account = get_account()
    withdraw.withdraw({"from": account})


def main():
    fund()
