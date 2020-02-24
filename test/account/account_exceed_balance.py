import unittest
import datetime
import json
import yaml


from app.account.account import Account
from app.transaction.transaction import Transaction
from app.violations.violations import InsufficientLimit


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.a_dict = {
            "active-card": "true",
            "available-limit": 80
        }
        self.account = Account(self.a_dict)
        self.config = yaml.load(open('config.yml'))
        #import ipdb; ipdb.set_trace()

    def test_account_exceed_balance(self):
        transaction_time = datetime.datetime.now()
        transaction_time_str = transaction_time.strftime(self.config["date_time_format"])
        test_transaction = dict()
        test_transaction["merchant"] = "Burger King"
        test_transaction["amount"] = 100
        test_transaction["time"] = transaction_time_str
        #print(json.dumps(test_transaction))
        transaction = Transaction(test_transaction, self.config["date_time_format"])
        self.assertEqual(self.account.validate_transaction(transaction), False)
        self.assertEqual(type(self.account.get_violations()[-1]), type(InsufficientLimit()))
        print(str(self.account))


    def tearDown(self):
        Account.instance = None


if __name__ == '__main__':
    unittest.main()
