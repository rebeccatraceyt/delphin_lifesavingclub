from django.test import TestCase, Client
from django.urls import reverse


class TestOrderReviewView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view_url_exists_at_desired_location(self):
        """ Test URL is in correct location """
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """ Test URL is accessible """
        response = self.client.get(reverse('order_review'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """ Test correct template """
        response = self.client.get(reverse('order_review'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/order_review.html')


class TestOrderDetailsView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view_url_exists_at_desired_location(self):
        """ Test URL is in correct location """
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """ Test URL is accessible """
        response = self.client.get(reverse('order_review'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """ Test correct template """
        response = self.client.get(reverse('order_review'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/order_review.html')


class TestOrderDetailsView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view_url_exists_at_desired_location(self):
        """ Test URL is in correct location """
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """ Test URL is accessible """
        response = self.client.get(reverse('order_review'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """ Test correct template """
        response = self.client.get(reverse('order_review'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/order_review.html')
