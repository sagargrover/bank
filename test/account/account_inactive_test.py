import unittest
import datetime
import json
import yaml


from app.account.account import Account
from app.transaction.transaction import Transaction
from app.violations.violations import CardNotActive


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.a_dict = {
            "active-card": "false",
            "available-limit": 80
        }
        self.account = Account(self.a_dict)
        self.config = yaml.load(open('config.yml'))
        #import ipdb; ipdb.set_trace()

    def test_account_creation(self):
        self.assertEqual(self.account.get_limit(), 80)
        self.assertEqual(self.account.get_card_status(), False)

    def test_one_transaction(self):
        transaction_time = datetime.datetime.now()
        transaction_time_str = transaction_time.strftime(self.config["date_time_format"])
        test_transaction = dict()
        test_transaction["merchant"] = "Burger King"
        test_transaction["amount"] = 20
        test_transaction["time"] = transaction_time_str
        #print(json.dumps(test_transaction))
        transaction = Transaction(test_transaction, self.config["date_time_format"])
        self.assertEqual(self.account.validate_transaction(transaction), False)
        self.assertEqual(type(self.account.get_violations()[-1]), type(CardNotActive()))


    def tearDown(self):
        Account.instance = None


if __name__ == '__main__':
    unittest.main()
