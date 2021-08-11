from django.apps import apps
from django.test import TestCase
from .apps import ShopConfig


class ShopConfig(TestCase):

    def test_app(self):
        self.assertEqual("shop", apps.get_app_config("shop").name)
