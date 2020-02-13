from django.test import TestCase


class WrapWithTestCase(TestCase):
    def test_true_is_true(self):
        self.assertTrue(True)
