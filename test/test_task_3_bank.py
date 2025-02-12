from src.task_3_bank import *

my_account = Bank(0,5)

def test_deposit():
    my_account.deposit(17000)
    my_account.deposit(-7000)
    assert my_account.checkbalance() == 10000

def test_withdraw():
    my_account.withdraw(4000)
    my_account.withdraw(-1000)
    assert my_account.checkbalance() == 7000


def test_checkbalance():
    assert my_account.checkbalance() == 7000


def test_apply_interest():
    assert my_account.apply_interest() == 350


def test_afford_to_pay_bill():
    assert my_account.afford_to_pay_bill(5000) == True
    assert my_account.afford_to_pay_bill(8000) == False