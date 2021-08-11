from django.test import TestCase
from django.urls import reverse, resolve
from .views import (
    shopping_bag,
    add_to_bag,
    update_bag,
    remove_from_bag
)


class TestUrls(TestCase):
    """ Tests for urls in cart app """

    def test_shopping_bag_url_is_resolved(self):
        url = reverse('shopping_bag')
        self.assertEqual(resolve(url).func, shopping_bag)

    def test_add_to_bag_url_is_resolved(self):
        url = reverse('add_to_bag', args=['test-item-id'])
        self.assertEqual(resolve(url).func, add_to_bag)

    def test_update_bag_url_is_resolved(self):
        url = reverse('update_bag', args=['test-item-id'])
        self.assertEqual(resolve(url).func, update_bag)

    def test_remove_from_bag_url_is_resolved(self):
        url = reverse('remove_from_bag', args=['test-item-id'])
        self.assertEqual(resolve(url).func, remove_from_bag)
