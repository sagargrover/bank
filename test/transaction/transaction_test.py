import unittest
import datetime
import yaml
import json

from app.transaction.transaction import Transaction


class TestTransactions(unittest.TestCase):
    def setUp(self):
        self.config = yaml.load(open('config.yml'))
        str = """{"transaction": {"merchant": "Burger King", "amount": 20, "time":"2019-02-13T10:00:00.001Z"}}"""
        self.input = json.loads(str).get('transaction')
        self.transaction = Transaction(self.input, self.config["date_time_format"])

    def test_transaction_data(self):
        self.assertEqual(self.transaction.get_amount(), 20)
        self.assertEqual(self.transaction.get_merchant(), "Burger King")
        self.assertEqual(self.transaction.get_time(), datetime.datetime(2019, 2, 13, 10, 0, 0, 1000))
        self.assertEqual(self.transaction.get_distinct_key(), "Burger King" + "#####" + str(20))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
