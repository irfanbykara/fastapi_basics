from app.calculations import add,subtract,BankAccount,InsufficientFunds
import pytest

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1,num2,expected_val",
                         [
                             (3,2,5),
                             (7,1,8),
                             (12,4,16)
                         ])
def test_hello(num1,num2,expected_val):
    print('Testing the add function hello...')
    sum = add (num1,num2)
    assert sum == expected_val

def test_subtract():
    print('Testing the subtract function...')
    remaining = subtract(10,6)
    assert remaining == 4

def test_bank_set_inital_amount(bank_account):

    assert bank_account.balance == 50

def test_deposit():
    bank_account = BankAccount(50)
    bank_account.deposit(30)
    assert bank_account.balance == 80

def test_collect_interest():
    bank_account = BankAccount(50)
    bank_account.collect_interest()
    assert round(bank_account.balance,6) == 55


@pytest.mark.parametrize("deposited,withdrew,expected_val",
                         [
                             (200,40,160),
                             (100,50,50),
                             (12,4,8)
                         ])

def test_bank_transaction(zero_bank_account,deposited,withdrew,expected_val):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected_val


def test_insufficient_funds(zero_bank_account):
    with pytest.raises(InsufficientFunds):
        zero_bank_account.withdraw(50)

