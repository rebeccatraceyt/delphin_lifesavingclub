from django.test import TestCase
from django.urls import reverse, resolve
from .views import (
    checkout,
    order_review,
    order_details,
    order_complete
)


class TestUrls(TestCase):
    """ Tests for urls in cart app """

    def test_checkout_url_is_resolved(self):
        url = reverse('checkout')
        self.assertEqual(resolve(url).func, checkout)

    def test_order_review_url_is_resolved(self):
        url = reverse('order_review')
        self.assertEqual(resolve(url).func, order_review)

    def test_order_details_url_is_resolved(self):
        url = reverse('order_details')
        self.assertEqual(resolve(url).func, order_details)

    def test_order_complete_url_is_resolved(self):
        url = reverse('order_complete', args=['test-order-id'])
        self.assertEqual(resolve(url).func, order_complete)
