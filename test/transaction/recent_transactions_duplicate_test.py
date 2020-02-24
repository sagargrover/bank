import unittest
import datetime
import yaml
from mock import patch

from app.violations.violations import DuplicateTransactionViolation
from app.transaction.transaction import Transaction
from app.transaction.recent_transactions import RecentTransactions


class TestRecentTransactions(unittest.TestCase):
    def setUp(self):
        self.config = yaml.load(open('config.yml'))
        self.date = datetime.datetime(2019, 2, 13, 10, 0, 0)
        self.datetime_obj = datetime.datetime
        delta = datetime.timedelta(minutes=2)
        self.recent_transactions = RecentTransactions(3, delta)

    def test_duplicate(self):
        with patch('datetime.datetime') as mock_date:
            mock_date.now.return_value = self.date
            mock_date.side_effect = lambda *args, **kw: self.datetime_obj(*args, **kw)

            # 1st transaction at edge of window
            transaction_time = datetime.datetime(2019, 2, 13, 9, 58, 0)
            transaction_time_str = transaction_time.strftime(self.config["date_time_format"])
            test_transaction = dict()
            test_transaction["merchant"] = "Burger King"
            test_transaction["amount"] = 20
            test_transaction["time"] = transaction_time_str
            transaction = Transaction(test_transaction, self.config["date_time_format"])
            self.assertEqual(self.recent_transactions.is_valid_transaction(transaction), (True, None))
            self.recent_transactions.add_recent_transaction(transaction)

            # 2nd transaction
            transaction_time = datetime.datetime(2019, 2, 13, 9, 59, 30)
            transaction_time_str = transaction_time.strftime(self.config["date_time_format"])
            test_transaction["amount"] = 21
            test_transaction["time"] = transaction_time_str
            transaction = Transaction(test_transaction, self.config["date_time_format"])
            self.assertEqual(self.recent_transactions.is_valid_transaction(transaction), (True, None))
            self.recent_transactions.add_recent_transaction(transaction)

            # 3rd transaction - repeat transaction
            transaction_time = datetime.datetime(2019, 2, 13, 9, 59, 50)
            transaction_time_str = transaction_time.strftime(self.config["date_time_format"])
            test_transaction["amount"] = 20
            test_transaction["time"] = transaction_time_str
            transaction = Transaction(test_transaction, self.config["date_time_format"])
            is_valid = self.recent_transactions.is_valid_transaction(transaction)
            self.assertEqual((is_valid[0], type(is_valid[1])), (False, type(DuplicateTransactionViolation())))



    def tearDown(self):
        self.recent_transactions = None


if __name__ == '__main__':
    unittest.main()
