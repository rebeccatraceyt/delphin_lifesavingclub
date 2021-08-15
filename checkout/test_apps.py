from django.apps import apps
from django.test import TestCase
from checkout.apps import CheckoutConfig


class CheckoutConfig(TestCase):

    def test_app(self):
        self.assertEqual("checkout", apps.get_app_config("checkout").name)
