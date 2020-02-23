import unittest
from app.violations.violations import DuplicateTransactionViolation, HighFrequencySmallIntervalViolation


class TestViolations(unittest.TestCase):
    def setUp(self):
        self.duplicate_violation = DuplicateTransactionViolation()
        self.high_frequency_violation = HighFrequencySmallIntervalViolation()

    def test_duplicate_violation(self):
        self.assertEqual(self.duplicate_violation.violation_code, 409)
        self.assertEqual(str(self.duplicate_violation), "doubled-transaction")

    def test_high_freq_violation(self):
        self.assertEqual(self.high_frequency_violation.violation_code, 429)
        self.assertEqual(str(self.high_frequency_violation), "high-frequency-small-interval")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
