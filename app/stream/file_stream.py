import json
import sys
import yaml
import logging.config

from settings import dictConfig

logging.config.dictConfig(dictConfig)
yaml.warnings({'YAMLLoadWarning': False})

from app.stream.base_stream import BaseStream
from app.account.account import Account
from app.transaction.transaction import Transaction
from app.violations.violations import AccountAlreadyIntialized


stream_logger = logging.getLogger('stream_logger')


class FileStream(BaseStream):
    def __init__(self):
        self.account = None

    def process_event(self, event):
        stream_logger.info("Event received - " + event)
        event_dict = json.loads(event)

        if "account" in event_dict:
            if not self.account:
                self.account = Account(event_dict.get('account'))
            else:
                self.account.add_violation(AccountAlreadyIntialized())
        elif "transaction" in event_dict:
            if not self.account:
                sys.stdout.write("account-not-initialized")
            else:
                self.account.validate_transaction(Transaction(event_dict.get('transaction')))

        if self.account:
            sys.stdout.write(str(self.account))

        sys.stdout.write('\n')

    def read_from_source(self, source):
        for line in source:
            self.process_event(line)
