from django.test import TestCase
from django.urls import reverse


class TestShoppingBagView(TestCase):
    def test_view_url_exists_at_desired_location(self):
        """ Test URL is in correct location """
        response = self.client.get('/shopping_bag/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """ Test URL is accessible """
        response = self.client.get(reverse('shopping_bag'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """ Test correct template """
        response = self.client.get(reverse('shopping_bag'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shopping_bag/shopping_bag.html')
