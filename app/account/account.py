import yaml
import datetime
import json
yaml.warnings({'YAMLLoadWarning': False})

from app.transaction.recent_transactions import RecentTransactions
from app.violations.violations import AccountAlreadyIntialized, InsufficientLimit, CardNotActive
from app.transaction.transaction import Transaction


class Account:
    def __init__(self, a_dict):
        self.__limit = float(a_dict.get('available-limit'))
        self.__has_active_card = (str(a_dict.get('active-card')).lower() == 'true')
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

    def deduct_amount(self, amount):
        self.__limit = self.__limit - amount

    def get_card_status(self):
        return self.__has_active_card

    def get_violations(self):
        return self.__violations

    def add_violation(self, violation):
        self.__violations.append(violation)

    def validate_transaction(self, transaction: Transaction):
        is_valid = True
        #print(transaction)
        if not self.get_card_status():
            self.add_violation(CardNotActive())
            is_valid = False
        #print(transaction.get_amount())
        if transaction.get_amount() > self.get_limit():
            self.add_violation(InsufficientLimit())
            is_valid = False

        is_valid_by_recent, violation = self.__recent_transactions.is_valid_transaction(transaction)
        if not is_valid_by_recent:
            self.add_violation(violation)
            is_valid = False
        if is_valid:
            self.__recent_transactions.add_recent_transaction(transaction)
            self.deduct_amount(transaction.get_amount())
        return is_valid


