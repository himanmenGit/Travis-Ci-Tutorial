from django.conf import settings
from django.test import TestCase


class ConfigTest(TestCase):
    def test_debug_true(self):
        self.assertEqual(settings.DEBUG, True)
