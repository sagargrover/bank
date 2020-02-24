import unittest
from app.violations.violations import DuplicateTransactionViolation, HighFrequencySmallIntervalViolation, CardNotActive, AccountAlreadyIntialized, InsufficientLimit


class TestViolations(unittest.TestCase):
    def setUp(self):
        self.duplicate_violation = DuplicateTransactionViolation()
        self.high_frequency_violation = HighFrequencySmallIntervalViolation()
        self.card_not_active_violation = CardNotActive()
        self.account_already_intialized_violation = AccountAlreadyIntialized()
        self.insufficent_limited_violation = InsufficientLimit()

    def test_duplicate_violation(self):
        self.assertEqual(self.duplicate_violation.violation_code, 409)
        self.assertEqual(str(self.duplicate_violation), "doubled-transaction")

    def test_high_freq_violation(self):
        self.assertEqual(self.high_frequency_violation.violation_code, 429)
        self.assertEqual(str(self.high_frequency_violation), "high-frequency-small-interval")

    def test_card_inactive_violation(self):
        self.assertEqual(self.card_not_active_violation.violation_code, 402)
        self.assertEqual(str(self.card_not_active_violation), "card-not-active")

    def test_insufficient_limit_violation(self):
        self.assertEqual(self.insufficent_limited_violation.violation_code, 401)
        self.assertEqual(str(self.insufficent_limited_violation), "insufficient-limit")

    def test_account_already_intialized_violation(self):
        self.assertEqual(self.account_already_intialized_violation.violation_code, 403)
        self.assertEqual(str(self.account_already_intialized_violation), "account-already-initialized")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
