import yaml
import datetime
import json

from app.transaction.recent_transactions import RecentTransactions
from app.violations.violations import AccountAlreadyIntialized,InsufficientLimit
from app.transaction.transaction import Transaction


class Account(object):

    class __Account:
        def __init__(self, a_dict):
            self.__limit = float(a_dict.get('available-limit'))
            self.__has_active_card = a_dict.get('active-card') == 'true'
            self.__violations = []
            self.config = yaml.load(open('config.yml'))
            delta = datetime.timedelta(hours=self.config["window_delta"]["hours"],
                                       minutes=self.config["window_delta"]["mins"],
                                       seconds=self.config["window_delta"]["seconds"]
                                       )
            window_size = self.config["window_size"]
            self.__recent_transactions = RecentTransactions(window_size=window_size, window_delta_time=delta)

        def __str__(self):
            return json.dumps({
                "account": {
                    "active-card": self.get_card_status(),
                    "available-limit": self.get_limit(),
                    "violations": [str(x) for x in self.get_violations()]
                }
            }, sort_keys=True)

        def get_limit(self):
            return self.__limit

        def set_limit(self, limit):
            self.__limit = limit

        def get_card_status(self):
            return self.__has_active_card

        def get_violations(self):
            return self.__violations

        def add_violation(self, violation):
            self.__violations.append(violation)

        def validate_transaction(self, transaction: Transaction):
            is_valid = True
            if not self.get_card_status():
                is_valid = False
            if transaction.get_amount() > self.get_limit():
                self.add_violation(InsufficientLimit())
                is_valid = False

            is_valid_by_recent, violation = self.__recent_transactions.is_valid_transaction(transaction)
            if not is_valid_by_recent:
                self.add_violation(violation)
                is_valid = False

            if is_valid:
                self.__recent_transactions.add_recent_transaction(transaction)
                self.set_limit(self.get_limit()-transaction.get_amount())

            return is_valid

    instance = None

    def __new__(cls, a_dict={}):
        if not Account.instance:
            Account.instance = Account.__Account(a_dict)
        else:
            Account.instance.add_violation(AccountAlreadyIntialized())
        return Account.instance
