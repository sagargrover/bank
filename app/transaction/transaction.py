import json
from datetime import datetime


class Transaction:
    def __init__(self, t_dict, time_stamp_format):
        #t_dict = json.loads(json_str).get('transaction')
        self.__merchant = t_dict.get('merchant')
        self.__amount = float(t_dict.get('amount'))
        self.__time = datetime.strptime(t_dict.get('time'), time_stamp_format)

    def get_amount(self):
        return self.__amount

    def get_merchant(self):
        return self.__merchant

    def get_time(self):
        return self.__time

    def get_distinct_key(self):
        return self.__merchant + "#####" + str(self.__amount)
