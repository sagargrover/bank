import datetime
from collections import deque

from app.violations.violations import DuplicateTransactionViolation, HighFrequencySmallIntervalViolation


class RecentTransactions:
    def __init__(self, window_size, window_delta_time):
        self.__window_size = window_size
        self.__window_delta_time = window_delta_time
        self.__queue = deque()
        self.__transactions_set = set()

    def in_window(self, transaction):
        transaction_time = transaction.get_time()
        current_time = datetime.datetime.now()
        print(current_time - transaction_time)
        if current_time - transaction_time <= self.__window_delta_time:
            return True
        return False

    def remove_expired_transaction(self):
        while len(self.__queue) != 0 and not self.in_window(self.__queue[0]):
            self.__transactions_set.discard(self.__queue[0].get_distinct_key())
            self.__queue.pop()

    def is_valid_transaction(self, transaction):
        self.remove_expired_transaction()
        if transaction.get_distinct_key() in self.__transactions_set:
                return False, DuplicateTransactionViolation()
        if len(self.__queue) == self.__window_size:
            return False, HighFrequencySmallIntervalViolation()
        return True, None

    def add_recent_transaction(self, transaction):
        self.__queue.append(transaction)
        self.__transactions_set.add(transaction.get_distinct_key())

