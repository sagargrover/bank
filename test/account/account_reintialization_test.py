import unittest
import datetime
import json
import yaml


from app.account.account import Account
from app.transaction.transaction import Transaction
from app.violations.violations import AccountAlreadyIntialized, InsufficientLimit


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.a_dict = {
            "active-card": "true",
            "available-limit": 80
        }
        self.account = Account(self.a_dict)
        self.config = yaml.load(open('config.yml'))

    def test_account_reintialization(self):
        self.account = Account(self.a_dict)
        self.assertEqual(type(self.account.get_violations()[-1]), type(AccountAlreadyIntialized()))

    def tearDown(self):
        Account.instance = None


if __name__ == '__main__':
    unittest.main()
