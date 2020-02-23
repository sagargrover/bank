import json
import sys

from app.stream.base_stream import BaseStream
from app.account.account import Account
from app.transaction.transaction import Transaction


class FileStream(BaseStream):

    def __init__(self):
        self.account = None

    def process_event(self, event):
        event_dict = json.loads(event)
        if "account" in event_dict:
            self.account = Account(event_dict)
        elif "transaction" in event_dict:
            if not self.account:
                sys.stdout.write("account-not-initialized")
            else:
                self.account.validate_transaction(Transaction(event_dict))

    def read_from_source(self):
        for line in sys.stdin:
            print(line)
