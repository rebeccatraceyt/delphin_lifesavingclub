from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from shop.models import Product
from django.contrib.auth.models import User


class TestOrderDetailsView(TestCase):
    def setUp(self):
        """ Creates user instance for login status """
        self.factory = RequestFactory()
        self.user = User.objects.create(username='testuser',
                                        email='test@email.com',
                                        password="testing321")

    def test_view_url_exists_at_desired_location(self):
        """ Test URL is in correct location """
        # login the user
        client = Client()
        client.login(username='testuser', password="testing789")

        response = self.client.get('/checkout/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """ Test URL is accessible """
        # login the user
        client = Client()
        client.login(username='testuser', password="testing789")

        response = self.client.get(reverse('order_review'))
        self.assertEqual(response.status_code, 302)

    def test_view_uses_correct_template(self):
        """ Test correct template redirects to all_products """
        # login the user
        client = Client()
        client.login(username='testuser', password="testing789")

        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/checkout/')

    def test_post_valid_order(self):
        """ Test order post """
        # login the user
        client = Client()
        client.login(username='testuser', password="testing789")

        # create an item
        item = Product.objects.create(name='test product',
                                      price='22',
                                      image='test.png',
                                      description='test desc',)

        # add item to cart
        self.client.post("/shopping_bag/add/{0}".format(item.id),
                         data={'quantity': '2'})

        # get the stripe publisable key
        stripe_id = 'tok_visa'

        # send the order
        response = self.client.post("/checkout/", {
            'full_name': 'name',
            'phone_number': '000',
            'email': 'test@test.com',
            'street_address1': 'address 1',
            'street_address2': 'address 2',
            'town_or_city': 'city',
            'county': 'county',
            'country': 'country',
            'postcode': 'code13',
            'credit_card_number': '4242424242424242',
            'cvv': '123',
            'expiry_month': '2',
            'expiry_year': '2022',
            'stripe_id': stripe_id},
            follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/accounts/login/?next=/checkout/')
