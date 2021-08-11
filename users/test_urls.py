from django.test import TestCase
from django.urls import reverse, resolve
from .views import (
    profile,
    order_history
)


class TestUrls(TestCase):
    """ Tests for urls in cart app """

    def test_profile_url_is_resolved(self):
        url = reverse('profile')
        self.assertEqual(resolve(url).func, profile)

    def test_order_history_url_is_resolved(self):
        url = reverse('order_history', args=['test-order-id'])
        self.assertEqual(resolve(url).func, order_history)
