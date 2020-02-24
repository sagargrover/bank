import unittest
import datetime
import yaml
from mock import patch


from app.stream.file_stream import FileStream
from app.utils.capture_stdout import Capturing


class TestFileStream(unittest.TestCase):
    def setUp(self):
        self.config = yaml.load(open('config.yml'))
        self.f = FileStream()
        self.date = datetime.datetime(2019, 2, 13, 10, 1, 0)
        self.datetime_obj = datetime.datetime


    @patch('datetime.datetime')
    def test_input_1(self, mock_date):
        mock_date.now.return_value = self.date
        mock_date.side_effect = lambda *args, **kw: self.datetime_obj(*args, **kw)
        inputs = [
            """{"account": {"active-card": true, "available-limit": 100}}""",
            """{"transaction": {"merchant": "Burger King", "amount": 20, "time":"2019-02-13T10:00:00.000Z"}}""",
            """{"transaction": {"merchant": "Habbib's", "amount": 90, "time":"2019-02-13T11:00:00.000Z"}}"""
        ]

        expected_output = [
            """{"account": {"active-card": true, "available-limit": 100.0, "violations": []}}""",
            """{"account": {"active-card": true, "available-limit": 80.0, "violations": []}}""",
            """{"account": {"active-card": true, "available-limit": 80.0, "violations": ["insufficient-limit"]}}"""
        ]

        with Capturing() as output:
            self.f.read_from_source(inputs)

        self.assertEqual(output, expected_output)

    @patch('datetime.datetime')
    def test_input_1(self, mock_date):
        mock_date.now.return_value = self.date
        mock_date.side_effect = lambda *args, **kw: self.datetime_obj(*args, **kw)
        inputs = [
            """{"account": {"active-card": true, "available-limit": 100}}""",
            """{"transaction": {"merchant": "Burger King", "amount": 20, "time":"2019-02-13T10:00:00.000Z"}}""",
            """{"transaction": {"merchant": "Habbib's", "amount": 90, "time":"2019-02-13T11:00:00.000Z"}}"""
        ]

        expected_output = [
            """{"account": {"active-card": true, "available-limit": 100.0, "violations": []}}""",
            """{"account": {"active-card": true, "available-limit": 80.0, "violations": []}}""",
            """{"account": {"active-card": true, "available-limit": 80.0, "violations": ["insufficient-limit"]}}"""
        ]

        with Capturing() as output:
            self.f.read_from_source(inputs)

        self.assertEqual(output, expected_output)

    @patch('datetime.datetime')
    def test_input_2(self, mock_date):
        mock_date.now.return_value = self.date
        mock_date.side_effect = lambda *args, **kw: self.datetime_obj(*args, **kw)
        inputs = [
            """{"account": {"active-card": true, "available-limit": 100}}""",
            """{"account": {"active-card": true, "available-limit": 350}}""",
        ]

        expected_output = [
            """{"account": {"active-card": true, "available-limit": 100.0, "violations": []}}""",
            """{"account": {"active-card": true, "available-limit": 100.0, "violations": ["account-already-initialized"]}}""",
        ]

        with Capturing() as output:
            self.f.read_from_source(inputs)

        self.assertEqual(output, expected_output)

    @patch('datetime.datetime')
    def test_input_3(self, mock_date):
        mock_date.now.return_value = self.date
        mock_date.side_effect = lambda *args, **kw: self.datetime_obj(*args, **kw)
        inputs = [

            """{"account": {"active-card": true, "available-limit": 100}}""",
            """{"transaction": {"merchant": "Burger King", "amount": 20, "time":"2019-02-13T10:00:00.000Z"}}""",
        ]

        expected_output = [
            """{"account": {"active-card": true, "available-limit": 100.0, "violations": []}}""",
            """{"account": {"active-card": true, "available-limit": 80.0, "violations": []}}""",
        ]

        with Capturing() as output:
            self.f.read_from_source(inputs)

        self.assertEqual(output, expected_output)

    @patch('datetime.datetime')
    def test_input_4(self, mock_date):
        mock_date.now.return_value = self.date
        mock_date.side_effect = lambda *args, **kw: self.datetime_obj(*args, **kw)
        inputs = [

            """{"account": {"active-card": true, "available-limit": 100}}""",
            """{"transaction": {"merchant": "Burger King", "amount": 20, "time":"2019-02-13T10:00:00.000Z"}}""",
            """{"transaction": {"merchant": "Burger King", "amount": 21, "time":"2019-02-13T10:00:00.000Z"}}""",
            """{"transaction": {"merchant": "Burger King", "amount": 22, "time":"2019-02-13T10:00:00.000Z"}}""",
            """{"transaction": {"merchant": "Habbib's", "amount": 90, "time":"2019-02-13T10:01:00.000Z"}}"""
        ]

        expected_output = [
            """{"account": {"active-card": true, "available-limit": 100.0, "violations": []}}""",
            """{"account": {"active-card": true, "available-limit": 80.0, "violations": []}}""",
            """{"account": {"active-card": true, "available-limit": 59.0, "violations": []}}""",
            """{"account": {"active-card": true, "available-limit": 37.0, "violations": []}}""",
            """{"account": {"active-card": true, "available-limit": 37.0, "violations": ["insufficient-limit", "high-frequency-small-interval"]}}"""
        ]

        with Capturing() as output:
            self.f.read_from_source(inputs)

        self.assertEqual(output, expected_output)


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
