from django.apps import apps
from django.test import TestCase
from .apps import ShoppingBagConfig


class ShoppingBagConfig(TestCase):

    def test_app(self):
        self.assertEqual("shopping_bag",
                         apps.get_app_config("shopping_bag").name)
