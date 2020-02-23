import unittest
import datetime
import yaml
import json
from app.violations.violations import HighFrequencySmallIntervalViolation, DuplicateTransactionViolation

from app.transaction.transaction import Transaction
from app.transaction.recent_transactions import RecentTransactions


class TestRecentTransactions(unittest.TestCase):
    def setUp(self):
        self.config = yaml.load(open('config.yml'))

    def test_high_freq(self):
        delta = datetime.timedelta(seconds=20)
        recent_transactions = RecentTransactions(3, delta)
        #datetime.datetime.now = Mock()
        #datetime.datetime.now = datetime.datetime(2019, 2, 13, 10, 0, 0)
        transaction_time = datetime.datetime.now()
        transaction_time_str = transaction_time.strftime(self.config["date_time_format"])
        test_transaction = dict()
        test_transaction["merchant"] = "Burger King"
        test_transaction["amount"] = 20
        test_transaction["time"] = transaction_time_str
        print(json.dumps(test_transaction))
        transaction = Transaction((test_transaction), self.config["date_time_format"])
        self.assertEqual(recent_transactions.is_valid_transaction(transaction), (True, None))
        recent_transactions.add_recent_transaction(transaction)

        transaction_time = datetime.datetime.now() + datetime.timedelta(minutes=1)
        transaction_time_str = transaction_time.strftime(self.config["date_time_format"])
        test_transaction["amount"] = 21
        test_transaction["time"] = transaction_time_str
        print(json.dumps(test_transaction))
        transaction = Transaction((test_transaction), self.config["date_time_format"])
        self.assertEqual(recent_transactions.is_valid_transaction(transaction), (True, None))
        recent_transactions.add_recent_transaction(transaction)

        transaction_time = datetime.datetime.now() + datetime.timedelta(minutes=1, seconds=30)
        transaction_time_str = transaction_time.strftime(self.config["date_time_format"])
        test_transaction["amount"] = 22
        test_transaction["time"] = transaction_time_str
        test_transaction["time"] = transaction_time_str
        print(json.dumps(test_transaction))
        transaction = Transaction((test_transaction), self.config["date_time_format"])
        self.assertEqual(recent_transactions.is_valid_transaction(transaction), (True, None))
        recent_transactions.add_recent_transaction(transaction)
        #sleep(20)
        transaction_time = datetime.datetime.now() + datetime.timedelta(minutes=3)
        transaction_time_str = transaction_time.strftime(self.config["date_time_format"])
        test_transaction["amount"] = 23
        test_transaction["time"] = transaction_time_str
        test_transaction["time"] = transaction_time_str
        print(json.dumps(test_transaction))
        transaction = Transaction((test_transaction), self.config["date_time_format"])
        is_valid = recent_transactions.is_valid_transaction(transaction)
        self.assertEqual((is_valid[0], type(is_valid[1])), (False, type(HighFrequencySmallIntervalViolation())))
        recent_transactions.add_recent_transaction(transaction)

    def test_duplicate(self):
        delta = datetime.timedelta(seconds=20)
        recent_transactions = RecentTransactions(3, delta)
        #datetime.datetime.now = Mock()
        #datetime.datetime.now = datetime.datetime(2019, 2, 13, 10, 0, 0)
        transaction_time = datetime.datetime.now()
        transaction_time_str = transaction_time.strftime(self.config["date_time_format"])
        test_transaction = dict()
        test_transaction = dict()
        test_transaction["merchant"] = "Burger King"
        test_transaction["amount"] = 20
        test_transaction["time"] = transaction_time_str
        print(json.dumps(test_transaction))
        transaction = Transaction((test_transaction), self.config["date_time_format"])
        self.assertEqual(recent_transactions.is_valid_transaction(transaction), (True, None))
        recent_transactions.add_recent_transaction(transaction)

        transaction_time = datetime.datetime.now() + datetime.timedelta(minutes=1)
        transaction_time_str = transaction_time.strftime(self.config["date_time_format"])
        test_transaction["amount"] = 21
        test_transaction["time"] = transaction_time_str
        print(json.dumps(test_transaction))
        transaction = Transaction((test_transaction), self.config["date_time_format"])
        self.assertEqual(recent_transactions.is_valid_transaction(transaction), (True, None))
        recent_transactions.add_recent_transaction(transaction)

        transaction_time = datetime.datetime.now() + datetime.timedelta(minutes=1, seconds=30)
        transaction_time_str = transaction_time.strftime(self.config["date_time_format"])
        test_transaction["amount"] = 20
        test_transaction["time"] = transaction_time_str
        test_transaction["time"] = transaction_time_str
        print(json.dumps(test_transaction))
        transaction = Transaction((test_transaction), self.config["date_time_format"])
        is_valid = recent_transactions.is_valid_transaction(transaction)
        self.assertEqual((is_valid[0], type(is_valid[1])), (False, type(DuplicateTransactionViolation())))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
