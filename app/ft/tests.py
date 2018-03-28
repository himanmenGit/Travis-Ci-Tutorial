from django.test import TestCase


class ConfigTest(TestCase):
    def test_failed(self):
        self.assertEqual(2, 3)
