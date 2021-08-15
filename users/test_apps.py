from django.apps import apps
from django.test import TestCase
from .apps import UsersConfig


class UsersConfig(TestCase):

    def test_app(self):
        self.assertEqual("users", apps.get_app_config("users").name)
