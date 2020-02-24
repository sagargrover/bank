import json
import yaml
from datetime import datetime


class Transaction:
    def __init__(self, t_dict, time_stamp_format=None):
        #t_dict = json.loads(json_str).get('transaction')
        if not time_stamp_format:
            config = yaml.load(open('config.yml'))
            time_stamp_format = config["date_time_format"]
        self.__merchant = t_dict.get('merchant')
        self.__amount = float(t_dict.get('amount'))
        self.__time = datetime.strptime(t_dict.get('time'), time_stamp_format)

    def __str__(self):
        return json.dumps({
            "merchant": self.get_merchant(),
            "amount": self.get_amount(),
            "time": str(self.get_time())
        }, sort_keys=True)

    def get_amount(self):
        return self.__amount

    def get_merchant(self):
        return self.__merchant

    def get_time(self):
        return self.__time

    def get_distinct_key(self):
        return self.__merchant + "#####" + str(int(self.__amount))
