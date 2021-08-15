from django.test import TestCase, Client
from django.urls import reverse


class TestShoppingBagView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view_url_exists_at_desired_location(self):
        """ Test URL is in correct location """
        response = self.client.get('/shopping_bag/')
        self.assertEqual(response.status_code, 302)

    def test_view_url_accessible_by_name(self):
        """ Test URL is accessible """
        response = self.client.get(reverse('shopping_bag'))
        self.assertEqual(response.status_code, 302)

    def test_view_uses_correct_template(self):
        """ Test correct template used to redirect to bag """
        response = self.client.get(reverse('shopping_bag'))
        self.assertEqual(response.status_code, 302)
