from django.apps import apps
from django.test import TestCase
from .apps import HomeConfig


class HomeConfig(TestCase):

    def test_app(self):
        self.assertEqual("pages", apps.get_app_config("pages").name)
